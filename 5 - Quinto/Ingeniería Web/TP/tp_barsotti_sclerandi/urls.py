from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'', include('content.urls')),
    url(r'', include('moderation.urls')),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^google77705fbceb081480\.html/$', TemplateView.as_view(template_name='google_property_verification.html', content_type='text/plain')),

    # API
    url(r'api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]