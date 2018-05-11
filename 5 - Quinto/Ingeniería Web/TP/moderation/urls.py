from django.conf.urls import url
from .views import moderation, reported_content_details, cancel_ban, confirm_ban, ajax_moderation_pagination, \
    comment_post_original, cancel_user_ban

urlpatterns = [
    url(r'^moderation/$', moderation, name='moderation'),
    url(r'^moderation/reported_content_details/(?P<content_id>\d+)/$', reported_content_details, name='reported_content_details'),
    url(r'^moderation/comment_post_original/(?P<comment_id>\d+)/(?P<post_id>\d+)/$', comment_post_original, name='comment_post_original'),
    url(r'^moderation/cancel_ban/$', cancel_ban, name='cancel_ban'),
    url(r'^moderation/cancel_user_ban/(?P<user_id>\d+)/$', cancel_user_ban, name='cancel_user_ban'),
    url(r'^moderation/confirm_ban$', confirm_ban, name='confirm_ban'),

    # Métodos Ajax
    url(r'^moderation/ajax_moderation_pagination', ajax_moderation_pagination, name='ajax_moderation_pagination'),
]