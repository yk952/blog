from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    # 1. 替换 list_display 中的 created_at/updated_at → create_time/update_time
    list_display = ('id', 'title', 'content', 'create_time', 'update_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # 2. 替换 list_filter 中的 created_at/updated_at → create_time/update_time
    list_filter = ('create_time', 'update_time')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)  # 分类的筛选字段无需修改

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
