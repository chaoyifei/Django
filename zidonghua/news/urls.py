from django.conf.urls import url
from news import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<news_body_id>\d+)/$', views.article, name='article'),
    #url(r'^del_article/(?P<news_body_id>\d+)/$', views.del_article, name='del_article'),
    #url(r'^staff/', views.staff, name='staff'),
    ]
urlpatterns += staticfiles_urlpatterns()