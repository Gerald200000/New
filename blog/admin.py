from django.contrib import admin
from .models import Post

class PostAd(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')

admin.site.register(Post, PostAd)
