from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_end, name='post_list_end'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/full/$', views.post_list, name='post_list'),
]