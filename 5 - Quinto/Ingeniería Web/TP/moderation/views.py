from .forms import BanForm
from content.models import Content
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse
from django.template.loader import render_to_string
from home.models import CustomUser
from home.utils import paginate, send_ban_mail, send_cancel_user_ban_mail
import json

@login_required(redirect_field_name='redirect')
def moderation(request):
    if request.user.is_admin:
        # Obtener contenido reportado.
        reported_posts_list = Content.get_reported_content_list(True)
        reported_comments_list = Content.get_reported_content_list(False)

        # Obtener lista de usuarios baneados.
        banned_users_list = CustomUser.get_banned_users_list()

        # Paginar la lista de posts.
        reported_posts_page = paginate(reported_posts_list, 1)
        reported_comments_page = paginate(reported_comments_list, 1)
        banned_users_page = paginate(banned_users_list, 1)

        return render(request, 'moderation/moderation.html', {'reported_posts_page': reported_posts_page,
                                                              'reported_comments_page': reported_comments_page,
                                                              'banned_users_page': banned_users_page })

    return redirect('index')

@login_required(redirect_field_name='redirect')
def reported_content_details(request, content_id):
    if request.user.is_admin:
        # Obtener detalle del contenido.
        content = Content.get_content_details_if_exists(content_id, True, False)

        # Obtener denuncias del contenido.
        complaints = content.complaint_set.all()

        # Formulario para el baneo.
        ban_form = BanForm()

        return render(request, 'moderation/reported_content_details.html', {'content': content,
                                                                            'complaints': complaints,
                                                                            'ban_form': ban_form })

    return redirect('index')

@login_required(redirect_field_name='redirect')
def comment_post_original(request, comment_id, post_id):
    if request.user.is_admin:
        # Obtener detalle del post.
        post = Content.get_post_original(post_id)
        try:
            comment_id = int(comment_id)
        except ValueError:
            raise Http404

        # Formulario para el baneo.
        ban_form = BanForm()

        return render(request, 'moderation/comment_post_original.html', {'post': post,
                                                                         'comment_id': comment_id,
                                                                         'ban_form': ban_form })

    return redirect('index')

@login_required(redirect_field_name='redirect')
def confirm_ban(request):
    if request.method == 'POST':
        ban_form = BanForm(request.POST)
        if ban_form.is_valid() and request.user.is_admin:
            content_id = ban_form.cleaned_data['content_id']
            try:
                ban_days = int(ban_form.cleaned_data['type_ban'])

                # Obtener contenido y eliminarlo.
                content = Content.get_content_details_if_exists(content_id, True, False)
                content.set_elimination_date()

                # Si el contenido era un post, eliminar sus comentarios, votos y favoritos relacionados.
                if content.response_to is None:
                    content.delete_content_relationships()

                # Banear al usuario.
                user = CustomUser.get_user(content.user.id)
                user.set_ban(ban_days)

                # Enviar mail de aviso al usuario.
                if ban_days != 0:
                    send_ban_mail(user, ban_days, content)

                return redirect('moderation')

            except ValueError:
                return redirect('index')

    return redirect('index')


@login_required(redirect_field_name='redirect')
def cancel_ban(request):
    if request.method == 'POST':
        if request.user.is_admin:
            try:
                content_id = int(request.POST['content_id'])

                # Obtener contenido.
                content = Content.get_content_details_if_exists(content_id, True, False)

                # Eliminar denuncias.
                content.complaint_set.all().delete()

                # Sacarle el ban al contenido.
                content.reported = False
                content.save()

            except ValueError:
                pass

            return redirect('moderation')

    return redirect('index')

@login_required(redirect_field_name='redirect')
def cancel_user_ban(request, user_id):
    if request.user.is_admin:
        # Obtener usuario y sacarle el baneo.
        user = CustomUser.get_user(user_id)
        user.state = CustomUser.UserProfileState.CONFIRMED.value
        user.save()

        # Enviar mail de aviso al usuario.
        send_cancel_user_ban_mail(user)

        return redirect('moderation')

    return redirect('index')

# Región - Métodos AJAX
@login_required(redirect_field_name='redirect')
def ajax_moderation_pagination(request):
    if request.method == 'POST':
        try:
            type = request.POST['type']
            page = int(request.POST['page_number'])

            # Obtener lista correspondiente y paginar.
            if type == 'post':
                response_list = Content.get_reported_content_list(True)
                template_name = 'moderation/_reported_posts.html'
                response_name = 'reported_posts_page'
            elif type == 'comment':
                response_list = Content.get_reported_content_list(False)
                template_name = 'moderation/_reported_comments.html'
                response_name = 'reported_comments_page'
            elif type == 'user':
                response_list = CustomUser.get_banned_users_list()
                template_name = 'moderation/_banned_users.html'
                response_name = 'banned_users_page'
            else:
                raise ValueError

            response_page = paginate(response_list, page)

            # Obtener HTML renderizado con la página indicada.
            html_content = render_to_string(template_name, { response_name: response_page, })

            response = {
                'success': True,
                'html': html_content,
            }

        except ValueError:
            response = {
                'success': False
            }

        return HttpResponse(json.dumps(response), content_type="application/json")

    return redirect('index')