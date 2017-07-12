# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import markdown

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
class NewsBody(models.Model):
    news_title = models.CharField(max_length=50)
    news_body = models.TextField()
    news_type = models.CharField(max_length=50)
    news_timestamp = models.DateTimeField()
    news_imgurl = models.CharField(max_length=50, null=True)
    news_author = models.CharField(max_length=20)
    def __str__(self):
        return self.news_title


admin.site.register(UserInfo)