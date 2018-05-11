from .views import register, activation, resend_activation_mail, login, profile, logout, edit_profile, \
    ajax_profile_posts_list, my_content, favorites, user_content, ajax_user_profile_posts_list
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^activation/(?P<token>.+)/$', activation, name='activation'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^favorites/$', favorites, name='favorites'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^my_content/$', my_content, name='my_content'),
    url(r'^user_content/(?P<user_id>\d+)/$', user_content, name='user_content'),
    url(r'^profile/(?P<user_id>\d+)/$', profile, name='profile'),
    url(r'^register/$', register, name='register'),
    url(r'^resend-activation-mail/(?P<token>.+)/$', resend_activation_mail, name='resend_activation_mail'),

    # Métodos Ajax
    url(r'^ajax_profile_posts_list$', ajax_profile_posts_list, name='ajax_profile_posts_list'),
    url(r'^ajax_user_profile_posts_list$', ajax_user_profile_posts_list, name='ajax_user_profile_posts_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)