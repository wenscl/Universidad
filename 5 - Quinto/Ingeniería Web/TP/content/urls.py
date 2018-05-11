from .views import create_post, ajax_upload_image, ajax_tag_suggestions, post_details, \
    edit_post, delete_post, comment_post, sections, section, index, ajax_complaint, \
    ajax_vote_post, delete_comment, ajax_favorite, edit_comment, item_suggestion, \
    create_list, edit_list, delete_list, restore_post
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^_edit_comment\.html/$', TemplateView.as_view(template_name='content/_edit_comment.html', content_type='text/plain')),
    url(r'^comment_post/(?P<post_id>\d+)/$', comment_post, name='comment_post'),
    url(r'^create_list/$', create_list, name='create_list'),
    url(r'^create_post/$', create_post, name='create_post'),
    url(r'^delete_comment/$', delete_comment, name='delete_comment'),
    url(r'^delete_list/(?P<list_id>\d+)/$', delete_list, name='delete_list'),
    url(r'^delete_post/(?P<post_id>\d+)/$', delete_post, name='delete_post'),
    url(r'^edit_comment/$', edit_comment, name='edit_comment'),
    url(r'^edit_list/(?P<list_id>\d+)/$', edit_list, name='edit_list'),
    url(r'^edit_post/(?P<post_id>\d+)/$', edit_post, name='edit_post'),
    url(r'^item_suggestion/$', item_suggestion, name='item_suggestion'),
    url(r'^post_details/(?P<post_id>\d+)/$', post_details, name='post_details'),
    url(r'^restore_post/(?P<post_id>\d+)/$', restore_post, name='restore_post'),
    url(r'^search/', include('haystack.urls')),
    url(r'^section/(?P<section_id>\d+)/$', section, name='section'),
    url(r'^sections/$', sections, name='sections'),

    # Métodos Ajax
    url(r'^ajax_complaint$', ajax_complaint, name='ajax_complaint'),
    url(r'^ajax_favorite$', ajax_favorite, name='ajax_favorite'),
    url(r'^ajax_tag_suggestions$', ajax_tag_suggestions, name='ajax_tag_suggestions'),
    url(r'^ajax_upload_image$', ajax_upload_image, name='ajax_upload_image'),
    url(r'^ajax_vote_post$', ajax_vote_post, name='ajax_vote_post'),
]