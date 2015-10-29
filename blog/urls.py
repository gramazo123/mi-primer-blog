from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),    
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalles_post),
    url(r'^post/nuevo/$', views.postear_nuevo, name='postear_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar_post, name='editar_post'),
]
