from haystack import indexes
from .models import Content


class ContentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    create_date = indexes.DateTimeField(model_attr='create_date')
    user_id = indexes.CharField(model_attr='user__id')
    user = indexes.CharField(model_attr='user__username')
    section = indexes.CharField(model_attr='section__name')
    section_id = indexes.IntegerField(model_attr='section__id')
    id = indexes.IntegerField(model_attr='id')
    content_score = indexes.FloatField(model_attr='score')
    vote_count = indexes.IntegerField(model_attr='vote_count')

    def get_model(self):
        return Content

    def index_queryset(self, using=None):
        # Indexar todos los post publicados y no eliminados.
        return self.get_model().objects.filter(elimination_date__isnull=True, published=True, response_to=None, reported=False)