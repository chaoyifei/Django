from django.conf.urls import patterns, url
from Photo import views
from zidonghua import  settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.ListView.as_view(), name='item_list'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='item_detail'),
    url(r'^photo/(?P<pk>\d+)/$', views.PhotoDetailView.as_view(), name='photo_detail'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()