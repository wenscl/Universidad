from .views import SectionViewSet, api_root, ContentViewSet, CustomUserViewSet, SearchViewSet, docs
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'sections', SectionViewSet, base_name='section')
router.register(r'contents', ContentViewSet, base_name='content')
router.register(r'users', CustomUserViewSet, base_name='customuser')
router.register(r'search', SearchViewSet, base_name='search')

urlpatterns = [
    url(r'^$', api_root),
    url(r'^docs/$', docs, name='docs'),
    url(r'^get_token/', views.obtain_auth_token),
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)