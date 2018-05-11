from .permissions import IsContentOwnerOrReadOnly, IsContentOwner, UserIsNotBanned,\
    IsNotContentOwner, IsProfileOwnerOrReadOnly
from .serializers import SectionSerializer, ContentSerializer, CustomUserReadSerializer, \
    ContentReadSerializer, CommentReadSerializer, CustomUserSerializer, VoteSerializer, \
    ContentTypes, CommentSerializer, ComplaintSerializer
from content.models import Section, Content, CustomUser
from django.conf import settings
from django.shortcuts import Http404, render
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from rest_framework import permissions, viewsets, mixins, status, serializers
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('customuser-list', request=request, format=format),
        'contents': reverse('content-list', request=request, format=format),
        'sections': reverse('section-list', request=request, format=format),
        'search': reverse('search-list', request=request, format=format),
    })

class SectionViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Section.get_sections_list()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsNotBanned)

    @detail_route()
    def content(self, request, pk=None):
        content_list = Section.get_posts_by_section_id(section_id=pk)
        serializer = ContentReadSerializer(content_list,
                                           many=True,
                                           context={'request': request})

        page = self.paginate_queryset(content_list)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsContentOwnerOrReadOnly,
                          UserIsNotBanned, )

    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('GET', ):
            return ContentReadSerializer

        return ContentSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Content.get_posts_list_published()
        elif self.action in ('update', 'partial_update'):
            return Content.objects.filter(elimination_date__isnull=True, reported=False)

        return Content.objects.filter(reported=False)

    def retrieve(self, request, *args, **kwargs):
        content = self.get_object()
        if content.response_to:
            serializer = CommentReadSerializer(content, context={'request': request})
        else:
            serializer = ContentReadSerializer(content, context={'request': request})

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        content_type = request.data.get('content_type', None)

        if not content_type:
            raise serializers.ValidationError({'content_type': ['Este campo es requerido.']})

        if content_type == ContentTypes.CONTENT.value:
            serializer = ContentSerializer(data=request.data, context={'request': request})
        else:
            serializer = CommentSerializer(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        # Obtener objeto
        instance = self.get_object()

        # Verificar que la request no esté vacía.
        if not request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Determinar tipo de contenido
        if not instance.response_to:
            request.data['content_type'] = ContentTypes.CONTENT.value
            serializer = ContentSerializer(instance=instance, data=request.data, partial=partial,
                                           context={'request': request})
        else:
            request.data['content_type'] = ContentTypes.COMMENT.value
            request.data['response_to'] = instance.response_to.id
            serializer = CommentSerializer(instance=instance, data=request.data, partial=partial,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_destroy(self, instance):
        if instance.elimination_date:
            raise Http404

        instance.set_elimination_date()
        # Si no se trata de un comentario, eliminar las relaciones.
        if not instance.response_to:
            instance.delete_content_relationships()

    # Vistas adicionales
    @detail_route()
    def comments(self, request, pk=None):
        content = self.get_object()
        comments = content.get_descendants()

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        serializer = CommentReadSerializer(comments, many=True, context={'request': request})
        
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def restore(self, request, pk=None):
        content = self.get_object()

        # Verificar que no se intente restaurar un contenido no eliminado o un comentario.
        if not content.elimination_date or content.response_to:
            raise Http404

        content.restore()
        serializer = ContentReadSerializer(content, context={'request': request})

        return Response(serializer.data)

    @list_route()
    def top10_posts(self, request):
        top10_posts, _ = Content.get_top10_of_last_week()
        serializer = ContentReadSerializer(top10_posts, many=True, context={'request': request})

        page = self.paginate_queryset(top10_posts)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    @list_route()
    def top10_lists(self, request):
        _, top10_lists = Content.get_top10_of_last_week()
        serializer = ContentReadSerializer(top10_lists, many=True, context={'request': request})

        page = self.paginate_queryset(top10_lists)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    @detail_route(methods=['post', 'delete'], permission_classes=[permissions.IsAuthenticated, IsNotContentOwner,])
    def vote(self, request, pk=None):

        content = self.get_object()

        # Verificar que el contenido solicitado no se encuentre eliminado y no sea comentario.
        if content.elimination_date or not content.published or content.response_to:
            raise Http404

        # Verificar si se desea eliminar una votación realizada.
        if request.method == 'DELETE':
            content.remove_vote(request.user)

            return Response(status=status.HTTP_204_NO_CONTENT)

        # Obtener valor de la votación.
        serializer = VoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.validated_data['rating']

        content.vote(user=request.user, rating=rating)

        return Response(serializer.data)

    @detail_route(methods=['post', 'delete'], permission_classes=[permissions.IsAuthenticated, IsNotContentOwner, ])
    def favorite(self, request, pk=None):

        content = self.get_object()

        # Verificar que el contenido solicitado no se encuentre eliminado y no sea comentario.
        if content.elimination_date or not content.published or content.response_to:
            raise Http404

        # Verificar si se desea eliminar un contenido de la lista de favoritos.
        if request.method == 'DELETE':
            request.user.remove_from_favorites(content=content)

            return Response(status=status.HTTP_204_NO_CONTENT)

        request.user.add_to_favorites(content=content)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post', ], permission_classes=[permissions.IsAuthenticated, IsNotContentOwner, ])
    def report(self, request, pk=None):
        content = self.get_object()

        # Verificar que el contenido solicitado no se encuentre eliminado y no sea un borrador.
        # Comprobar si el usuario ya realizó una queja al mismo contenido.
        if content.elimination_date or (not content.response_to and not content.published) or request.user.complaint_set.filter(content__id=content.id).exists():
            raise Http404

        # Obtener descripión del reporte.
        serializer = ComplaintSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        complaint = serializer.validated_data['comment']

        request.user.add_complaint(content=content, comment=complaint)

        return Response(serializer.data)

class CustomUserViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = CustomUser.objects.filter(state__in=[CustomUser.UserProfileState.CONFIRMED.value, CustomUser.UserProfileState.TEMPORARILY_BANNED.value])
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsNotBanned, IsProfileOwnerOrReadOnly)
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('GET', ):
            return CustomUserReadSerializer

        return CustomUserSerializer

    @detail_route(permission_classes=[permissions.IsAuthenticatedOrReadOnly, UserIsNotBanned])
    def published_content(self, request, pk=None):
        user = self.get_object()
        published_content = Content.get_content_list_for_user(user=user,
                                                              is_published=True,
                                                              is_deleted=False)
        page = self.paginate_queryset(published_content)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        serializer = ContentReadSerializer(published_content, many=True, context={'request': request})

        return Response(serializer.data)

    @detail_route(permission_classes=[IsContentOwner])
    def content_drafts(self, request, pk=None):
        user = self.get_object()
        content_drafts = Content.get_content_list_for_user(user=user,
                                                           is_published=False,
                                                           is_deleted=False)
        page = self.paginate_queryset(content_drafts)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        serializer = ContentReadSerializer(content_drafts, many=True, context={'request': request})

        return Response(serializer.data)

    @detail_route(permission_classes=[IsContentOwner])
    def recycle_bin(self, request, pk=None):
        user = self.get_object()
        recycle_bin = Content.get_content_list_for_current_user(user=user,
                                                                is_published=None,
                                                                is_deleted=True,
                                                                is_list=None)
        page = self.paginate_queryset(recycle_bin)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        serializer = ContentReadSerializer(recycle_bin, many=True, context={'request': request})

        return Response(serializer.data)

    @detail_route(permission_classes=[IsContentOwner])
    def favorites(self, request, pk=None):
        user = self.get_object()
        favorites = user.get_favorites_list()
        page = self.paginate_queryset(favorites)
        if page is not None:
            serializer = ContentReadSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        serializer = ContentReadSerializer(favorites, many=True, context={'request': request})

        return Response(serializer.data)

class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ContentReadSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = EmptySearchQuerySet()

        if request.GET.get('q') is not None:
            query = request.GET.get('q')
            queryset = SearchQuerySet().filter(content=query)

        queryset = Content.objects.filter(pk__in=(x.pk for x in queryset))

        return queryset

def docs(request):
    return render(request, 'api/docs.html', { 'domain': settings.DOMAIN_URL })