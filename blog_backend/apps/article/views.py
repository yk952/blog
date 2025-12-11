from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer


# 1. 文章过滤类（保持不变，用于按分类筛选）
class ArticleFilter(django_filters.FilterSet):
    """按分类ID过滤文章"""
    category = django_filters.NumberFilter(field_name='category__id')  # 关联分类ID

    class Meta:
        model = Article
        fields = ['category']  # 支持的过滤字段


# 2. 文章视图集（合并重复定义，保留所有功能）
class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图集：支持CRUD + 分类筛选 + 动态权限
    """
    # 序列化器：文章数据转换
    serializer_class = ArticleSerializer
    # 过滤配置：启用分类筛选
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter  # 使用自定义过滤类
    # 优化查询：关联查询作者和分类（减少数据库请求）
    queryset = Article.objects.all().select_related('author', 'category').order_by('-create_time')

    def get_permissions(self):
        """
        动态权限控制：
        - 发布/修改/删除文章：需登录（IsAuthenticated）
        - 查看文章列表/详情：允许匿名访问（AllowAny）
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]  # 登录才能操作
        return [permissions.AllowAny()]  # 匿名可查看

    def perform_create(self, serializer):
        """发布文章时，自动关联当前登录用户为作者（解决author_id为空问题）"""
        serializer.save(author=self.request.user)  # 从请求中获取当前登录用户


# 3. 分类视图集（保留，可根据需求调整权限）
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # 权限：当前设置为"登录后可访问"，若需匿名查看分类，可改为动态权限
    # 例如：def get_permissions(self): ...（参考ArticleViewSet的权限逻辑）
    permission_classes = [permissions.IsAuthenticated]