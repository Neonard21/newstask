from django.contrib import admin
from .models import NewsArticle, NewsTag

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(NewsTag)
