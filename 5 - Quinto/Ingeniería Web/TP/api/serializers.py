from rest_framework import serializers
from django.db.models import Q
from django.shortcuts import Http404, get_object_or_404
from content.models import Section, Content, Tag, CustomUser, ListItem, LISTS_SECTION_NAME, Vote
from home.models import Complaint
from enum import Enum

class ContentTypes(Enum):
    CONTENT = 'content'
    COMMENT = 'comment'

# Section Serializers
class SectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'url', 'name', 'description')

# Content Serializers
class ContentSectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'url', 'name')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('text', )

class ContentTagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('text', )

class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = ('item_id', 'item_name', 'item_type')

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    content_type = serializers.ChoiceField(choices=[member.value for name, member in ContentTypes.__members__.items()], write_only=True)
    tags = TagSerializer(many=True, required=False)
    items = ListItemSerializer(many=True, required=False)
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = Content
        fields = (
            'content_type', 'id', 'url', 'title', 'description', 'create_date',
            'section', 'published', 'tags', 'items'
        )
        extra_kwargs = {'title': {'required': True} }

    def create(self, validated_data):
        # Quitar content_type.
        validated_data.pop('content_type')

        # Obtener los tags a partir de la información validada (si es que se proporcionan).
        tags = validated_data.pop('tags', [])

        # Obtener los items a partir de la información validada (si es que se proporcionan).
        items = validated_data.pop('items', [])

        # Crear contenido.
        content = Content.objects.create(user=self.context['request'].user, **validated_data)

        # Guardar los Tags.
        tag_list = []
        for tag in tags:
            content_tag = Tag.get_or_create_tag(tag['text'])
            tag_list.append(content_tag)

        content.tags.set(tag_list, clear=False)

        # Guardar los Items.
        for item_data in items:
            ListItem.objects.create(content=content, **item_data)

        return content

    def update(self, instance, validated_data):
        if instance.elimination_date:
            raise Http404

        if not instance.published:
            instance.published = validated_data.get('published', instance.published)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.section = validated_data.get('section', instance.section)
        instance.save()

        # Guardar los Tags.
        if 'tags' in validated_data.keys():
            # Obtener los tags a partir de la información validada (si es que se proporcionan).
            tags = validated_data.pop('tags')
            tag_list = []
            for tag in tags:
                content_tag = Tag.get_or_create_tag(tag['text'])
                tag_list.append(content_tag)

            instance.tags.set(tag_list, clear=False)

        # Guardar los Items.
        if 'items' in validated_data.keys():
            ListItem.objects.filter(content=instance).delete()
            # Obtener los items a partir de la información validada (si es que se proporcionan).
            items = validated_data.pop('items')
            for item_data in items:
                ListItem.objects.create(content=instance, **item_data)

        return instance

    def validate(self, data):
        if self.instance:
            if self.instance.section.name == LISTS_SECTION_NAME and data.get('section', self.instance.section).name != LISTS_SECTION_NAME:
                raise serializers.ValidationError({'section': ['No es posible modificar la sección de una lista.']})
            if self.instance.section.name != LISTS_SECTION_NAME and data.get('section', self.instance.section).name == LISTS_SECTION_NAME:
                raise serializers.ValidationError({'section': ['No es posible modificar la sección de un post a \'{}\'.'.format(LISTS_SECTION_NAME)]})
            if data.get('section', self.instance.section).name == LISTS_SECTION_NAME and 'items' in data.keys() and not data['items']:
                raise serializers.ValidationError({'items': ['La lista debe contener, al menos, una película o serie.', ]})
            if data.get('published', self.instance.published) is None:
                raise serializers.ValidationError({'published': ['Este campo no puede ser nulo.',]})
        else:
            if 'section' in data.keys() and data['section'].name == LISTS_SECTION_NAME and ('items' not in data.keys() or not data['items']):
                raise serializers.ValidationError({'items': ['La lista debe contener, al menos, una película o serie.',]})

            if data.get('published', None) is None:
                raise serializers.ValidationError({'published': ['Este campo es requerido y no puede ser nulo.',]})

        return data

class ContentUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'url', 'username', )

class ContentReadSerializer(serializers.ModelSerializer):
    user = ContentUserSerializer()
    section = ContentSectionSerializer()
    tags = serializers.StringRelatedField(many=True)
    score = serializers.ReadOnlyField()
    vote_count = serializers.ReadOnlyField()
    items = ListItemSerializer(many=True)

    class Meta:
        model = Content
        fields = (
            'id', 'url', 'title', 'description', 'user', 'create_date',
            'last_modification_date', 'elimination_date', 'section',
            'published', 'score', 'vote_count', 'tags', 'items'
        )

# Comments Serializers
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    content_type = serializers.ChoiceField(choices=[member.value for name, member in ContentTypes.__members__.items()], write_only=True)
    response_to = serializers.PrimaryKeyRelatedField(queryset=Content.objects.filter(Q(published=True)|Q(published=None, response_to__isnull=False)))

    class Meta:
        model = Content
        fields = (
            'content_type', 'id', 'url', 'description', 'create_date', 'response_to'
        )

    def create(self, validated_data):
        # Quitar content_type.
        validated_data.pop('content_type')

        comment = Content.objects.create(user=self.context['request'].user, **validated_data)

        return comment

    def validate(self, data):
        if not self.instance:
            _ = Content.get_content_details_if_exists(content_id=data['response_to'].id, is_reported=False, is_post=False)

        return data


class CommentReadSerializer(serializers.HyperlinkedModelSerializer):
    description = serializers.ReadOnlyField(source='actual_description')
    user = ContentUserSerializer()

    class Meta:
        model = Content
        fields = (
            'id', 'url', 'user', 'description', 'create_date', 'last_modification_date',
            'elimination_date', 'response_to', 'reported'
        )

# CustomUser Serializers
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'url', 'username', 'first_name', 'last_name', 'email',
            'date_of_birth', 'profile_image',
        )

class CustomUserReadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'url', 'username', 'first_name', 'last_name', 'email', 'state',
            'is_admin', 'date_joined', 'date_of_birth', 'profile_image',
        )

class VoteSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Vote
        fields = ( 'rating', )

class ComplaintSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(min_length=10, max_length=500)

    class Meta:
        model = Complaint
        fields = ( 'comment', )


class ContentSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = (
            'id', 'url', 'title', 'description', 'user', 'create_date',
            'last_modification_date', 'elimination_date', 'section',
            'published', 'score', 'vote_count', 'tags', 'items'
        )