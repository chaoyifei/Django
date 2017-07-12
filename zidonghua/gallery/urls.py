from gallery import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
]
urlpatterns += staticfiles_urlpatterns()