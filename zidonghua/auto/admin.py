'''
from django.contrib import admin
from auto.models import  AutoBody
# Register your models here.
class AutoBodyAdmin(admin.ModelAdmin):
    list_display = ('auto_title','auto_author','auto_timestamp')
    list_filter =['auto_timestamp']
    search_fields = ['auto_title']

admin.site.register(AutoBody,AutoBodyAdmin)

class PhotoInline(admin.TabularInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
'''


