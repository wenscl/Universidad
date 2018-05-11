from .forms import LoginForm, EditProfileForm, UserRegisterForm
from .models import CustomUser
from .utils import send_activation_mail, paginate
from content.models import Content
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.template.loader import render_to_string
from django.utils.timezone import localtime
import json

def register(request):
    # Comprobar que no haya un usuario actualmente logueado.
    if request.user.is_authenticated():
        return redirect('index')

    if request.method == 'POST':
        # Recuperar forms desde request.
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Crear usuario.
            user = CustomUser.objects.create_user(username=user_form.cleaned_data['username'],
                                                  email=user_form.cleaned_data['email'],
                                                  password=user_form.cleaned_data['password1'],)

            # Establecer estado del profile en "Pendiente de Confirmacion".
            user.state = CustomUser.UserProfileState.CONFIRMATION_PENDING.value

            # Generar clave y enviar mail de activacion
            send_activation_mail(user)

            return render(request, 'home/register_success.html', {'username': user.username, 'email': user.email })
    else:
        user_form = UserRegisterForm()

    return render(request, 'home/register.html', { 'user_form': user_form })

def activation(request, token):
    resend_mail = False

    # Obtener el perfil de usuario que tiene como activation key el token de la request.
    user = CustomUser.get_user_token(token)

    # Verificar que no haya expirado la validez de la key.
    if user.key_expiration_date > datetime.now(timezone.utc):
        # Eliminar clave de activacion y fecha de expiracion de la misma.
        user.activation_key = None
        user.key_expiration_date = None

        # Modificar el estado del perfil de usuario.
        user.state = CustomUser.UserProfileState.CONFIRMED.value

        # Guardar los cambios.
        user.save()

        auth_login(request, user)

    else:
        # Ofrecer la posibilidad de reenviar el mail en caso de que la key haya expirado.
        resend_mail = True

    return render(request, 'home/activation.html', { 'resend_mail': resend_mail, 'token': token })

def resend_activation_mail(request, token):
    # Generar nuevamente la clave de activacion y volver a enviar el mail de confirmacion.
    user = CustomUser.get_user_token(token)
    send_activation_mail(user)

    return render(request, 'home/resend_activation_mail.html', { 'username': user.username, 'email': user.email })

def login(request):
    if request.method == 'POST':
        redirect_url = request.POST['redirect_url']

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # Verificar que las credenciales sean validas, que el usuario este activo y que el estado del usuario sea 'Confirmado'.
            user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    if user.is_confirmed:
                        # Realizar el login
                        auth_login(request, user)

                        # Redirigir a la pagina en la que se encontraba (o al inicio)
                        if redirect_url:
                            return redirect(redirect_url)
                        else:
                            return redirect('index')
                    elif user.is_confirmation_pending:
                        login_form.add_error(None, 'El usuario no fue confirmado aún. Por favor, confirmá tu cuenta para poder ingresar.')
                    elif user.is_temporarily_banned:
                        login_form.add_error(None, 'El usuario fue baneado temporalmente. Podrás ingresar nuevamente el {:%d/%m/%Y a las %H:%M hs}.'.format(
                            localtime(user.temporary_ban_end_date)))
                    else:
                        login_form.add_error(None, 'El usuario fue baneado permanentemente. Contactá a un administrador para obtener más información.')
                else:
                    login_form.add_error(None, 'El usuario ingresado ya no existe. Por favor, contactá a un administrador.')
            else:
                login_form.add_error(None, 'Las credenciales ingresadas no son válidas. Por favor, intentalo nuevamente.')
    else:
        if request.user.is_authenticated:
            return redirect('index')

        redirect_url = request.GET.get('redirect')
        login_form = LoginForm()

    return render(request, 'home/login.html', { 'login_form': login_form, 'redirect_url': redirect_url })

def logout(request):
    auth_logout(request)

    return redirect('index')

@login_required(redirect_field_name='redirect')
def my_content(request):
    # Obtener post publicados y borradores, y listas publicadas y borradores.
    published_posts = Content.get_content_list_for_current_user(user=request.user.id,
                                                                is_published=True,
                                                                is_deleted=False,
                                                                is_list=False)
    drafts_posts = Content.get_content_list_for_current_user(user=request.user.id,
                                                             is_published=False,
                                                             is_deleted=False,
                                                             is_list=False)
    published_lists = Content.get_content_list_for_current_user(user=request.user.id,
                                                                is_published=True,
                                                                is_deleted=False,
                                                                is_list=True)
    drafts_lists = Content.get_content_list_for_current_user(user=request.user.id,
                                                             is_published=False,
                                                             is_deleted=False,
                                                             is_list=True)
    recicle_bin = Content.get_content_list_for_current_user(user=request.user.id,
                                                            is_published=True,
                                                            is_deleted=True,
                                                            is_list=False)

    # Paginar la lista de posts.
    published_posts_page = paginate(published_posts, 1)
    drafts_posts_page = paginate(drafts_posts, 1)
    published_lists_page = paginate(published_lists, 1)
    drafts_content_lists_page = paginate(drafts_lists, 1)
    recicle_bin_page = paginate(recicle_bin, 1)

    return render(request, 'home/my_content.html', { 'published_posts_page': published_posts_page,
                                                     'drafts_posts_page': drafts_posts_page,
                                                     'published_lists_page': published_lists_page,
                                                     'drafts_content_lists_page': drafts_content_lists_page ,
                                                     'recicle_bin_page': recicle_bin_page })

def user_content(request, user_id):
    # Obtener post y listas publicadas.
    published_posts = Content.get_content_list_for_current_user(user=user_id,
                                                                is_published=True,
                                                                is_deleted=False,
                                                                is_list=False)
    published_lists = Content.get_content_list_for_current_user(user=user_id,
                                                                is_published=True,
                                                                is_deleted=False,
                                                                is_list=True)

    # Obtener usuario
    user = CustomUser.get_user(user_id)

    # Paginar la lista de posts.
    published_posts_page = paginate(published_posts, 1)
    published_lists_page = paginate(published_lists, 1)

    return render(request, 'home/user_content.html', { 'published_posts_page': published_posts_page,
                                                       'published_lists_page': published_lists_page,
                                                       'user_profile': user })

def profile(request, user_id):
    user_profile = CustomUser.get_user(user_id)

    return render(request, 'home/profile.html', {'user_profile': user_profile})

@login_required(redirect_field_name='redirect')
def edit_profile(request):
    # Obtener usuario.
    user_profile = CustomUser.get_user(request.user.id)

    if request.method == 'POST':
        # Recuperar forms desde request.
        user_form = EditProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid():
            user = user_form.save()

            auth_login(request, user)

            return redirect(reverse('profile', kwargs={ 'user_id': user_profile.id }))

        return render(request, 'home/edit_profile.html', {'user_form': user_form})
    else:
        # Crear formulario a partir del post guardado.
        user_form = EditProfileForm(instance=user_profile)

    return render(request, 'home/edit_profile.html', { 'user_form' : user_form })

@login_required(redirect_field_name='redirect')
def favorites(request):
    # Obtener lista de favoritos.
    user = request.user
    favorites_list = user.get_favorites_list()

    # Paginar la lista de favoritos.
    page = request.GET.get('page')
    favorites_page = paginate(favorites_list, page)

    return render(request, 'home/favorites.html', { 'favorites_page': favorites_page })

# Región - Métodos AJAX
@login_required(redirect_field_name='redirect')
def ajax_profile_posts_list(request):
    if request.method == 'POST':
        try:
            page = int(request.POST['page_number'])
            is_published = request.POST['is_published'] == 'true'
            is_deleted = request.POST['is_deleted'] == 'true'
            is_list = request.POST['is_list'] == 'true'

            # Obtener lista de posts.
            content_list = Content.get_content_list_for_current_user(user=request.user.id,
                                                                     is_published=is_published,
                                                                     is_deleted=is_deleted,
                                                                     is_list=is_list)

            # Paginar la lista de posts.
            content_page = paginate(content_list, page)

            # Obtener HTML renderizado con la página indicada.
            html_content = render_to_string('content/_profile_post.html', { 'content_page': content_page,
                                                                            'is_published': str(is_published).lower(),
                                                                            'is_deleted': str(is_deleted).lower(),
                                                                            'is_list': str(is_list).lower() })

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

@login_required(redirect_field_name='redirect')
def ajax_user_profile_posts_list(request):
    if request.method == 'POST':
        try:
            user_id = int(request.POST['user_id'])
            page = int(request.POST['page_number'])
            is_list = request.POST['is_list'] == 'true'

            # Obtener lista de posts.
            content_list = Content.get_content_list_for_current_user(user=user_id,
                                                                     is_published=True,
                                                                     is_deleted=False,
                                                                     is_list=is_list)

            # Paginar la lista de posts.
            posts = paginate(content_list, page)

            # Obtener HTML renderizado con la página indicada.
            html_content = render_to_string('content/_user_posts_list.html', { 'posts': posts,
                                                                               'is_list': str(is_list).lower(),
                                                                               'user_id': user_id })

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