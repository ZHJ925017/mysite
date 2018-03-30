# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Category,Page,BlogPost,BlogPostAdmin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','views','likes')
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','url','views')

# Register your models here.
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)