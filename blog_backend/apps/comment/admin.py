from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'article', 'user', 'content')
    search_fields = ('article__title', 'user__username', 'content')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
