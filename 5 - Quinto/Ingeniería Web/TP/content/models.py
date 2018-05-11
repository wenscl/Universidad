from .tmdb_api_wrapper import GetItemTitle
from datetime import datetime, timedelta, timezone
from django.db import models
from home.models import CustomUser
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import get_object_or_404

class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    @staticmethod
    def get_sections_list():
        return Section.objects.all().order_by('id')

    @staticmethod
    def get_posts_by_section_id(section_id):
        section = get_object_or_404(Section, id=section_id)
        return [post for post in section.contents.all().order_by('-create_date') if post.published and post.elimination_date is None and not post.reported]

    def __str__(self):
        return self.name

# Nombre de la sección 'Listas'.
LISTS_SECTION_NAME = 'Listas'

class Tag(models.Model):
    text = models.CharField(max_length=50, verbose_name='Texto')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    # Obtener sugerencias de tags.
    @staticmethod
    def get_tag_suggestions(query):
        return [{"id": tag.text, "text": tag.text} for tag in Tag.objects.filter(text__icontains=query)]

    @staticmethod
    def get_or_create_tag(tag):
        # Recuperar un tag existente de la base de datos o crearlo si no existe.
        tag_obj, created = Tag.objects.get_or_create(text=tag.lower().strip())

        return tag_obj

    def __str__(self):
        return self.text

class Content(MPTTModel):
    title = models.CharField(max_length=100, verbose_name='Título', null=True, blank=True)
    description = models.TextField(verbose_name='Descripción')
    user = models.ForeignKey(CustomUser, related_name='created_content')
    create_date = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
    last_modification_date = models.DateTimeField(verbose_name='Fecha de Modificación', auto_now=True)
    section = models.ForeignKey(Section, related_name='contents', null=True, blank=True)
    elimination_date = models.DateTimeField(verbose_name='Fecha de Eliminación', null=True, blank=True)
    response_to = TreeForeignKey('self', related_name='responses', db_index=True, null=True, blank=True)
    published = models.NullBooleanField(verbose_name='Publicar')
    reported = models.BooleanField(verbose_name='Eliminado por denuncias', default=False)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='content', db_table='ContentTag', blank=True)
    votes = models.ManyToManyField(CustomUser, related_name='votes', through='Vote')

    # Determina el valor real de la descripción de un comentario, verificando si el mismo fue eliminado o reportado.
    @property
    def actual_description(self):
        if self.reported:
            if self.elimination_date:
                return 'Este comentario fue eliminado por la comunidad.'
            else:
                return 'Este comentario fue reportado por la comunidad y está en proceso de revisión.'
        elif self.elimination_date:
            return 'Este comentario fue eliminado por su autor.'

        return self.description

    # Determinar si el contenido se trata de una lista o de un post.
    @property
    def is_list(self):
        return self.section.name == LISTS_SECTION_NAME

    # Calcular el puntaje de un post.
    @property
    def score(self):
        vote_list = [vote.value for vote in self.vote_set.all()]
        if vote_list:
            return round(sum(vote_list) / float(len(vote_list)), 2)
        return 0

    # Calcular la cantidad de votos de un post.
    @property
    def vote_count(self):
        return self.vote_set.all().count()

    # Calcular la cantidad de denuncias de un contenido.
    @property
    def number_of_complaints(self):
        return self.complaints.count()

    # Indica si el contenido fue editado o no. Se hace de esta manera porque siempre existe una diferencia de microsegundos entre las fechas a comparar.
    @property
    def edited(self):
        return self.create_date + timedelta(seconds=5) < self.last_modification_date

    # Obtener lista de post publicados y no eliminados, ordenados por fecha de creación.
    @staticmethod
    def get_posts_list_published():
        return Content.objects.filter(response_to=None,
                                      elimination_date__isnull=True,
                                      published=True,
                                      reported=False).order_by('-create_date')

    # Obtener el contenido reportado y no eliminado.
    @staticmethod
    def get_reported_content_list(is_post):
        if is_post:
            return Content.objects.filter(elimination_date__isnull=True,
                                          reported=True,
                                          response_to=None)

        return Content.objects.filter(elimination_date__isnull=True,
                                      reported=True,
                                      response_to__isnull=False)

    # Obtener detalle de un contenido.
    @staticmethod
    def get_post_original(content_id):
        return get_object_or_404(Content,
                                 id=content_id,
                                 elimination_date__isnull=True)

    # Obtener detalle de un contenido.
    @staticmethod
    def get_content_details_if_exists(content_id, is_reported, is_post):
        if is_post:
            return get_object_or_404(Content,
                                     id=content_id,
                                     response_to=None,
                                     elimination_date__isnull=True,
                                     reported=is_reported)

        return get_object_or_404(Content,
                                 id=content_id,
                                 reported=is_reported,
                                 elimination_date__isnull=True)

    # Obtener detalle de un contenido, verificar que no esté eliminado y que el autor sea el usuario indicado.
    @staticmethod
    def get_user_content(content_id, user, is_post, is_deleted):
        if is_post:
            if is_deleted:
                return get_object_or_404(Content,
                                         user=user,
                                         id=content_id,
                                         response_to=None,
                                         elimination_date__isnull=False,
                                         reported=False)

            return get_object_or_404(Content,
                                     user=user,
                                     id=content_id,
                                     response_to=None,
                                     elimination_date__isnull=True,
                                     reported=False)

        return get_object_or_404(Content,
                                 user=user,
                                 id=content_id,
                                 response_to__isnull=False,
                                 elimination_date__isnull=True,
                                 reported=False)

    @staticmethod
    def get_content_list_for_current_user(user, is_published, is_deleted, is_list):
        if not is_deleted:
            if is_list:
                return Content.objects.filter(user=user,
                                              elimination_date__isnull=True,
                                              published=is_published,
                                              section__name=LISTS_SECTION_NAME,
                                              response_to=None,
                                              reported=False).order_by('-create_date')

            return Content.objects.filter(user=user,
                                          elimination_date__isnull=True,
                                          published=is_published,
                                          response_to=None,
                                          reported=False).exclude(section__name=LISTS_SECTION_NAME).order_by('-create_date')

        return Content.objects.filter(user=user,
                                      elimination_date__isnull=False,
                                      response_to=None,
                                      reported=False).order_by('-elimination_date')

    # Obtener lista de contenido de un usuario, sin distinción entre Posts y Listas.
    @staticmethod
    def get_content_list_for_user(user, is_published, is_deleted):
        return Content.objects.filter(user=user,
                                      elimination_date__isnull=not is_deleted,
                                      published=is_published,
                                      response_to=None,
                                      reported=False).order_by('-create_date')

    # Obtener los 10 post y listas más votados de la semana.
    @staticmethod
    def get_top10_of_last_week():
        posts = Content.objects.filter(elimination_date__isnull=True,
                                       published=True,
                                       reported=False,
                                       response_to=None,
                                       create_date__gte=datetime.now(timezone.utc) - timedelta(days=7)).exclude(section__name=LISTS_SECTION_NAME)
        top10_posts = sorted([post for post in posts if post.score > 0], key=lambda post: -post.score)[:10]

        lists = Content.objects.filter(section__name=LISTS_SECTION_NAME,
                                       elimination_date__isnull=True,
                                       published=True,
                                       reported=False,
                                       response_to=None,
                                       create_date__gte=datetime.now(timezone.utc) - timedelta(days=7))
        top10_lists = sorted([post for post in lists if post.score > 0], key=lambda post: -post.score)[:10]

        return top10_posts, top10_lists

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    class MPTTMeta:
        order_insertion_by = ['create_date']
        parent_attr = 'response_to'

    # Marcar el contenido como reportado.
    def set_ban(self):
        self.reported = True
        self.save()

    # Establecer la fecha de eliminación del contenido.
    def set_elimination_date(self):
        self.elimination_date = datetime.now(timezone.utc)
        self.save()

    # Eliminar los comentarios del post, los votos y favoritos relacionados.
    def delete_content_relationships(self):
        self.get_children().delete()
        self.vote_set.all().delete()
        self.favoritecontent_set.all().delete()
        Content.objects.rebuild()

    # Restaurar contenido.
    def restore(self):
        self.elimination_date = None
        self.save()

    # Votar el contenido.
    def vote(self, user, rating):
        # Verificar la existencia de un voto del usuario actual al post indicado.
        if self.vote_set.filter(user=user).exists():
            # Actualizar votación.
            vote = self.vote_set.get(user=user)
            vote.value = rating
            vote.save()
        else:
            # Agregar votación.
            self.vote_set.create(user=user, content=self, value=rating)

    # Eliminar una votación realizada sobre el contenido.
    def remove_vote(self, user):
        # Verificar la existencia de un voto del usuario actual al post indicado.
        if self.vote_set.filter(user=user).exists():
            # Obtener voto realizado y eliminarlo.
            self.vote_set.get(user=user).delete()

    def __str__(self):
        return str(self.id) + ' - ' + str(self.create_date)

class Vote(models.Model):
    user = models.ForeignKey(CustomUser)
    content = models.ForeignKey(Content)
    value = models.PositiveIntegerField(verbose_name='Valor')

    class Meta:
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'

    def __str__(self):
        return self.user.username

class ListItem(models.Model):
    content = models.ForeignKey(Content, related_name='items')
    item_id = models.CharField(verbose_name='Id del Item', max_length=100)
    item_name = models.CharField(verbose_name='Nombre del item', max_length=500)
    item_type = models.CharField(verbose_name='Tipo de item', max_length=50)

    @staticmethod
    def SaveItemList(item_list, content):
        # Eliminar los items que tiene asignada esa lista.
        ListItem.objects.filter(content=content).delete()

        # Agregar los items de la lista recibida como parámetro.
        for item in item_list:
            item_id, item_type = item.split(':')
            # Obtener información adicional del item.
            item_details = GetItemTitle(item_id, item_type)

            list_item = ListItem(content=content,
                                 item_id=item_id,
                                 item_name=item_details['title'],
                                 item_type=item_type, )
            list_item.save()

    class Meta:
        verbose_name = 'Ítem de lista'
        verbose_name_plural = 'Ítems de lista'

    def __str__(self):
        return '{}-{}: {} ({})'.format(self.content.id, self.item_id, self.item_name, self.item_type)