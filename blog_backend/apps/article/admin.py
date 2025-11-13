from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
