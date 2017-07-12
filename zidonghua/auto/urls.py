from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf.urls import url
from auto import views

urlpatterns = [
    url(r'^team', views.team, name='team'),
    url(r'^member', views.member, name='member'),
    url(r'^research', views.research, name='research'),
    url(r'^lab_gallery', views.lab_gallery, name='lab_gallery'),
    url(r'^contact', views.contact,name='contact'),
    url(r'^$', views.index,name='index'),
    ]
urlpatterns += staticfiles_urlpatterns()