#! -*- encoding:utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^about_me', views.about_me, name='about_me'),
    url(r'^posts/search/$', views.full_search, name='full_search'),
    url(r'^posts/upload/$', views.upload, name='upload'),
    url(r'^posts/add_category/$', views.add_category, name='upload'),
    url(r'^posts/category/(?P<cg>\w+)$', views.post_list_by_category, name='list_by_cg'),
    url(r'^site_media/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'static/upload/images/'}),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]
