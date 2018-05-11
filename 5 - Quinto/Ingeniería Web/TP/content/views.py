from .forms import PostForm, CommentForm, ListForm
from .models import Content, Tag, Section, ListItem, LISTS_SECTION_NAME
from .tmdb_api_wrapper import SearchMulti, GetItemTitle, GetItemsDetails
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from home.forms import ComplaintForm
from home.models import CustomUser
from home.utils import paginate
import json

COMPLAINTS_LIMIT = 10

def index(request):
    # Obtener el top 10 de posts y listas de la semana.
    top10_posts, top10_lists = Content.get_top10_of_last_week()

    # Obtener lista de posts publicados.
    posts_list = Content.get_posts_list_published()

    #Obtener número de página y paginar la lista de post.
    page = request.GET.get('page')
    posts_page = paginate(posts_list, page)

    return render(request, 'content/index.html', { 'posts_page': posts_page, 'top10_posts': top10_posts, 'top10_lists': top10_lists })

@login_required(redirect_field_name='redirect')
def create_post(request):
    if request.method == 'POST':
        # Recuperar form desde request.
        content_form = PostForm(request.POST)
        if content_form.is_valid():
            content = content_form.save(commit=False)
            content.user = request.user
            content.section = content_form.cleaned_data['section']
            content.save()

            # Guardar los items.
            if 'items' in content_form.cleaned_data.keys():
                items = [item_id_and_type for item_id_and_type in content_form.cleaned_data['items'].split(',') if item_id_and_type]
                ListItem.SaveItemList(item_list=items, content=content)

            # Guardar los tags del post.
            tags = [Tag.get_or_create_tag(tag) for tag in content_form.cleaned_data['tags'].split(',') if tag]
            content.tags.set(tags, clear=False)

            return redirect(reverse('post_details', kwargs={ 'post_id': content.id }))

        # Generar la lista de tags.
        tag_list = content_form.cleaned_data['tags']

        # Generar la lista de items con nombre y id.
        item_list = []
        if 'items' in content_form.cleaned_data.keys():
            item_list = [GetItemTitle(item_id_and_type.split(':')[0], item_id_and_type.split(':')[1])
                         for item_id_and_type in content_form.cleaned_data['items'].split(',') if item_id_and_type]

        return render(request, 'content/create_edit_post.html', {'content_form': content_form,
                                                                 'item_list': item_list,
                                                                 'tag_list': tag_list, })

    else:
        content_form = PostForm()

    return render(request, 'content/create_edit_post.html', { 'content_form' : content_form })

def post_details(request, post_id):
    # Obtener post.
    post = Content.get_content_details_if_exists(post_id, False, True)

    # Un post es visible si está publicado. Si no, solo el creador podrá verlo.
    if post.published or request.user == post.user:
        # Se crea el formulario para los comentarios.
        comment_form = CommentForm()
        comment_form.initial['response_to_id'] = post_id

        # Se crea el formulario para las denuncias.
        complaint_form = ComplaintForm()

        # Obtener la valoración actual del usuario logueado para este post.
        fav = False
        current_rating = 0
        if request.user.is_authenticated:
            if post.vote_set.filter(user=request.user).exists():
                current_rating = post.vote_set.get(user=request.user).value

            fav = request.user.favoritecontent_set.filter(content=post).exists()

        # Obtener información correspondiente a las películas y series relacionadas.
        items = GetItemsDetails([(item.item_id, item.item_type) for item in post.items.all()])

        return render(request, 'content/post_details.html', { 'post': post,
                                                              'comment_form': comment_form,
                                                              'current_rating': current_rating,
                                                              'complaint_form': complaint_form,
                                                              'fav': fav,
                                                              'items': items, })

    else:
        raise Http404

@login_required(redirect_field_name='redirect')
def edit_post(request, post_id):
    # Obtener post.
    post = Content.get_user_content(content_id=post_id, user=request.user, is_post=True, is_deleted=False)

    if request.method == 'POST':
        # Recuperar form desde request.
        content_form = PostForm(request.POST, instance=post)

        published_previous_state = post.published

        if content_form.is_valid():
            content = content_form.save(commit=False)

            content.section = content_form.cleaned_data['section']

            # Si el post estaba guardado (no publicado) y se publica, se actualiza la fecha de creación.
            if not published_previous_state and content.published:
                content.create_date = datetime.now(timezone.utc)
            else:
                content.published = published_previous_state

            content.save()

            # Guardar los items del post. Eliminar los cargados anteriormente.
            if 'items' in content_form.cleaned_data.keys():
                items = [item_id_and_type for item_id_and_type in content_form.cleaned_data['items'].split(',') if
                         item_id_and_type]
                ListItem.SaveItemList(item_list=items, content=content)

            # Guardar los tags del post.
            tags = [Tag.get_or_create_tag(tag) for tag in content_form.cleaned_data['tags'].split(',') if tag]
            content.tags.set(tags, clear=False)

            return redirect(reverse('post_details', kwargs={'post_id': content.id}))

        # Generar la lista de tags.
        tag_list = content_form.cleaned_data['tags']

        # Generar la lista de items con nombre y id.
        item_list = []
        if 'items' in content_form.cleaned_data.keys():
            item_list = [GetItemTitle(item_id_and_type.split(':')[0], item_id_and_type.split(':')[1])
                         for item_id_and_type in content_form.cleaned_data['items'].split(',') if item_id_and_type]
    else:
        # Crear formulario a partir del post guardado.
        content_form = PostForm(instance=post)

        # Establecer el valor del campo Tagsinput.
        tag_list = ','.join([tag.text for tag in post.tags.all()])

        # Si el post está publicado, no se permite des-publicarlo.
        if post.published:
            content_form.fields['published'].disabled = True

        # Generar la lista de items con nombre y id.
        item_list = [GetItemTitle(item.item_id, item.item_type) for item in content_form.instance.items.all()]

    return render(request, 'content/create_edit_post.html', { 'content_form' : content_form,
                                                              'item_list': item_list,
                                                              'tag_list': tag_list, })

@login_required(redirect_field_name='redirect')
def delete_post(request, post_id):
    # Obtener post.
    post = Content.get_user_content(content_id=post_id, user=request.user, is_post=True,is_deleted=False)

    if request.method == 'POST':
        post.set_elimination_date()

        # Eliminar los comentarios del post, los votos y favoritos relacionados.
        post.delete_content_relationships()

        return redirect('my_content')
    else:
        return render(request, 'content/confirm_delete.html', {'content': post})

@login_required(redirect_field_name='redirect')
def restore_post(request, post_id):
    # Obtener post y borrarle la fecha de eliminación.
    post = Content.get_user_content(content_id=post_id, user=request.user, is_post=True, is_deleted=True)
    post.restore()

    return redirect(reverse('post_details', kwargs={'post_id': post.id}))

@login_required(redirect_field_name='redirect')
def comment_post(request, post_id):
    if request.method == 'POST':
        # Recuperar form desde request.
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # Verificar que exista el post/comentario al que se intenta responder.
            content_response_to = Content.get_content_details_if_exists(comment_form.cleaned_data['response_to_id'], False, False)

            # Guardar comentario.
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.response_to = content_response_to

            comment.save()

            return redirect(reverse('post_details', kwargs={'post_id': post_id}))

        post = Content.objects.get(id=post_id)
        return render(request, 'content/post_details.html', { 'post': post, 'comment_form': comment_form })

    return redirect(reverse('post_details', kwargs={'post_id': post_id}))

@login_required(redirect_field_name='redirect')
def edit_comment(request):
    if request.method == 'POST':
        try:
            # Obtener id del comentario a editar.
            comment_id = int(request.POST['comment_id'])

            # Obtener comentario
            comment = Content.get_content_details_if_exists(comment_id, False, False)

            # Verificar que el usuario actual sea el autor del comentario a editar.
            if comment.user != request.user:
                raise Http404

            # Recuperar form desde request.
            comment_form = CommentForm(request.POST, instance=comment)

            if comment_form.is_valid():
                # Guardar comentario.
                comment_form.save()

            return redirect(reverse('post_details', kwargs={ 'post_id': comment.get_root().id }))

        except ValueError:
            raise Http404

    return redirect('index')

@login_required(redirect_field_name='redirect')
def delete_comment(request):
    if request.method == 'POST':
        try:
            # Obtener id del comentario a eliminar.
            comment_id = int(request.POST['comment_id'])

        except ValueError:
            # Error en el id del comentario.
            return redirect('index')

        # Obtener comentario.
        comment = Content.get_user_content(content_id=comment_id, user=request.user, is_post=False, is_deleted=False)

        # Obtener id del post al que pertenece el comentario.
        post_id = comment.get_root().id

        # Eliminar comentario.
        comment.set_elimination_date()

        # Redirigir nuevamente al detalle del post.
        return redirect(reverse('post_details', kwargs={'post_id': post_id}))

    return redirect('index')

def sections(request):
    # Obtener la lista de Secciones existentes.
    sections_list = Section.get_sections_list()

    return render(request, 'content/sections.html', { 'sections_list': sections_list })

def section(request, section_id):
    # Obtener la lista de posts para la sección especificada.
    posts_list = Section.get_posts_by_section_id(section_id)
    current_section = Section.objects.get(id=section_id)

    # Paginar la lista de post.
    page = request.GET.get('page')
    posts_page = paginate(posts_list, page)

    return render(request, 'content/section.html', { 'section': current_section, 'posts_page': posts_page })

@login_required(redirect_field_name='redirect')
def create_list(request):
    if request.method == 'POST':
        # Recuperar form desde request.
        list_form = ListForm(request.POST)

        if list_form.is_valid():
            content = list_form.save(commit=False)
            content.user = request.user
            content.section = Section.objects.get(name=LISTS_SECTION_NAME)
            content.save()

            # Guardar los items de la lista.
            items = [item_id_and_type for item_id_and_type in list_form.cleaned_data['items'].split(',') if item_id_and_type]
            ListItem.SaveItemList(item_list=items, content=content)

            # Guardar los tags de la lista.
            tags = [Tag.get_or_create_tag(tag) for tag in list_form.cleaned_data['tags'].split(',') if tag]
            content.tags.set(tags, clear=False)

            return redirect(reverse('post_details', kwargs={ 'post_id': content.id }))

        # Generar la lista de tags.
        tag_list = list_form.cleaned_data['tags']

        # Generar la lista de items con nombre y id.
        item_list = []
        if 'items' in list_form.cleaned_data.keys():
            item_list = [GetItemTitle(item_id_and_type.split(':')[0], item_id_and_type.split(':')[1])
                          for item_id_and_type in list_form.cleaned_data['items'].split(',') if item_id_and_type]

        return render(request, 'content/create_edit_list.html', { 'list_form' : list_form,
                                                                  'item_list': item_list,
                                                                  'tag_list': tag_list, })
    else:
        list_form = ListForm()

    return render(request, 'content/create_edit_list.html', { 'list_form' : list_form })

@login_required(redirect_field_name='redirect')
def edit_list(request, list_id):
    # Obtener lista.
    content_list = Content.get_user_content(content_id=list_id, user=request.user, is_post=True, is_deleted=False)

    if request.method == 'POST':
        # Recuperar form desde request.
        list_form = ListForm(request.POST, instance=content_list)

        published_previous_state = content_list.published

        if list_form.is_valid():
            edited_list = list_form.save(commit=False)

            # Si la lista estaba guardada (no publicada) y se publica, se actualiza la fecha de creación.
            if not published_previous_state and edited_list.published:
                edited_list.create_date = datetime.now(timezone.utc)
            else:
                edited_list.published = published_previous_state

            edited_list.save()

            # Guardar los items de la lista. Eliminar los cargados anteriormente.
            if 'items' in list_form.cleaned_data.keys():
                items = [item_id_and_type for item_id_and_type in list_form.cleaned_data['items'].split(',') if item_id_and_type]
                ListItem.SaveItemList(item_list=items, content=edited_list)

            # Guardar los tags de la lista.
            tags = [Tag.get_or_create_tag(tag) for tag in list_form.cleaned_data['tags'].split(',') if tag]
            edited_list.tags.set(tags, clear=False)

            return redirect(reverse('post_details', kwargs={'post_id': edited_list.id}))

        # Generar la lista de tags.
        tag_list = list_form.cleaned_data['tags']

        # Generar la lista de items con nombre y id.
        item_list = []
        if 'items' in list_form.cleaned_data.keys():
            item_list = [GetItemTitle(item_id_and_type.split(':')[0], item_id_and_type.split(':')[1])
                          for item_id_and_type in list_form.cleaned_data['items'].split(',') if item_id_and_type]
    else:
        # Crear formulario a partir de la lista guardada.
        list_form = ListForm(instance=content_list)

        # Establecer el valor del campo Tagsinput.
        tag_list = ','.join([tag.text for tag in content_list.tags.all()])

        # Si la lista está publicada, no se permite des-publicarla.
        if content_list.published:
            list_form.fields['published'].disabled = True

        # Generar la lista de items con nombre y id.
        item_list = [GetItemTitle(item.item_id, item.item_type) for item in list_form.instance.items.all()]

    return render(request, 'content/create_edit_list.html', {'list_form' : list_form,
                                                             'item_list': item_list,
                                                             'tag_list': tag_list, })

@login_required(redirect_field_name='redirect')
def delete_list(request, list_id):
    # Obtener lista.
    content_list = Content.get_user_content(content_id=list_id, user=request.user, is_post=True, is_deleted=False)

    if request.method == 'POST':
        content_list.set_elimination_date()

        # Eliminar los comentarios del post, los votos y favoritos relacionados.
        content_list.delete_content_relationships()

        return redirect('my_content')
    else:
        # Generar la lista de items con nombre y id.
        item_list = [GetItemTitle(item.item_id, item.item_type) for item in content_list.items.all()]

        return render(request, 'content/confirm_delete.html', {'content': content_list,
                                                               'item_list': item_list, })

def item_suggestion(request):
    # Obtener query desde request.
    query = request.GET['query']

    # Consultar API para obtener resultados.
    results = SearchMulti(query)

    return HttpResponse(results, content_type="application/json")

# Región - Métodos AJAX
def ajax_upload_image(request):
    # Se verifica que el método sea Post y que la imagen se haya recibido.
    if request.method == 'POST' and request.FILES['image']:
        # Se almacena la imagen en el servidor.
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # Se arma la respuesta JSON para el componente Summernote.
        response = {
            'url': uploaded_file_url,
            'filename': filename,
            'success': True,
        }
    else:
        response = {
            'success': False,
        }

    return HttpResponse(json.dumps(response), content_type="application/json")

def ajax_tag_suggestions(request):
    # Obtener parámetro de búsqueda.
    query = request.GET.get('q', None)

    # Obtener sugerencias de tags.
    json_response = Tag.get_tag_suggestions(query=query)

    return HttpResponse(json.dumps(json_response), content_type="application/json")

@login_required(redirect_field_name='redirect')
def ajax_complaint(request):
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            # Comprobar si el usuario ya realizó una queja al mismo contenido.
            if request.user.complaint_set.filter(content__id=complaint_form.cleaned_data['content_id']).exists():
                response_title = 'No se ha podido enviar la denuncia.'
                response_description = 'Ya realizaste una queja sobre este contenido.'
            else:
                # Obtener el contenido a denunciar.
                content = Content.get_content_details_if_exists(complaint_form.cleaned_data['content_id'], False, False)

                # Agregar denuncia.
                request.user.add_complaint(content=content, comment=complaint_form.cleaned_data['comment'])

                response_title = 'La denuncia se ha enviado exitosamente.'
                response_description = '¡Gracias por hacer del sitio un lugar mejor!'

                # Verificar cantidad de denuncias al mismo contenido.
                if content.number_of_complaints >= COMPLAINTS_LIMIT and not content.user.is_banned:
                    # Marcar el contenido como reportado.
                    content.set_ban()

        else:
            response_title = 'No se ha podido enviar la denuncia.'
            response_description = 'Por favor, comprobá los datos ingresados e intentalo nuevamente. Recordá que el comentario es obligatorio. :)'

        response = {
            'title': response_title,
            'description': response_description,
        }

        return HttpResponse(json.dumps(response), content_type="application/json")

    return redirect('index')

@login_required(redirect_field_name='redirect')
def ajax_vote_post(request):
    if request.method == 'POST':
        try:
            rating = int(request.POST['rating'])
            post_id = int(request.POST['post_id'])

            # Obtener Post a valorar.
            post = Content.get_content_details_if_exists(content_id=post_id, is_reported=False, is_post=True)

            # Verificar que el usuario no sea el creador del post.
            if request.user == post.user:
                raise ValueError

            # Determinar si se desea puntuar el post o eliminar una votación ya realizada.
            if rating == 0:
                # Se desea eliminar una votación.
                post.remove_vote(user=request.user)
            else:
                # Se desea realizar una votación.
                post.vote(user=request.user, rating=rating)

            response = {
                'success': True,
                'new_score': post.score,
                'vote_count': '({} {})'.format(post.vote_count, 'voto' if post.vote_count == 1 else 'votos'),
            }

        except ValueError:
            response = {
                'success': False
            }

        return HttpResponse(json.dumps(response), content_type="application/json")


    return redirect('index')

@login_required(redirect_field_name='redirect')
def ajax_favorite(request):
    if request.method == 'POST':
        try:
            post_id = int(request.POST['post_id'])

            content = Content.get_content_details_if_exists(post_id, False, True)
            if request.user != content.user:
                user = CustomUser.get_user(request.user.id)

                # Eliminar el favorito si ya existe.
                if user.favoritecontent_set.filter(content=content).exists():
                    user.remove_from_favorites(content=content)
                    response = {
                        'success': True,
                        'fav': False
                    }
                else:
                    user.add_to_favorites(content=content)
                    response = {
                        'success': True,
                        'fav': True
                    }
            else:
                response = {
                    'success': False
                }

        except ValueError:
            response = {
                'success': False
            }

        return HttpResponse(json.dumps(response), content_type="application/json")

    return redirect('index')