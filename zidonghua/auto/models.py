# -*- coding: utf-8 -*-
'''
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from django.db.models import permalink
from zidonghua.fields import ThumbnailImageField
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.
#用户信息
class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    def __str__(self):
        return self.nickname

#消息信息
class AutoBody(models.Model):
    auto_title = models.CharField(max_length=50)
    auto_body = models.TextField()
    auto_type = models.CharField(max_length=50)
    auto_timestamp = models.DateTimeField()
    auto_imgurl = models.CharField(max_length=50, null=True)
    auto_author = models.CharField(max_length=20)
    def __str__(self):
        return self.auto_title

#图片信息

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'pk': self.id})


class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})

#admin.site.register(AutoBody)
admin.site.register(UserInfo)
'''