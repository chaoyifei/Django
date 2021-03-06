"""zidonghua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf.urls import url,include
from django.contrib import admin
from zidonghua import  settings
from django.conf.urls.static import static
import os


urlpatterns = [
    url(r'^auto/', include('auto.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^Photo/', include('Photo.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^news/', include('news.urls')),


]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.IMAGE_PREFIX, document_root=os.path.join(settings.MEDIA_ROOT, settings.IMAGE_PREFIX))