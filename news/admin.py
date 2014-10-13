from __future__ import unicode_literals
from django.contrib import admin
from news.models import News, DeletedNews

# Register your models here.
admin.site.register(News)
admin.site.register(DeletedNews)