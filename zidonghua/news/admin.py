from django.contrib import admin
from news.models import  NewsBody
# Register your models here.
class NewsBodyAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_author','news_timestamp')
    list_filter =['news_timestamp']
    search_fields = ['news_title']

admin.site.register(NewsBody,NewsBodyAdmin)



