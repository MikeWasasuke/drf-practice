from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'content', 'author', 'owner')


admin.site.register(Post, PostAdmin)
