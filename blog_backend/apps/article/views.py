from rest_framework import viewsets, permissions  # 统一导入permissions模块
from django_filters.rest_framework import DjangoFilterBackend  # 导入分类筛选依赖
from .models import Article, Category  # 导入Article和Category模型（筛选需用到Category）
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图集：基于ModelViewSet实现完整的CRUD操作
    自动支持：
    - GET /articles/：列表查询（list）
    - GET /articles/{id}/：单篇查询（retrieve）
    - POST /articles/：发布文章（create）
    - PUT /articles/{id}/：修改文章（update）
    - PATCH /articles/{id}/：部分修改（partial_update）
    - DELETE /articles/{id}/：删除文章（destroy）
    """
    # 查询集：所有文章，按创建时间倒序（最新文章在前）
    queryset = Article.objects.all().order_by('-create_time')
    # 序列化器：指定用于数据转换的序列化器
    serializer_class = ArticleSerializer
    # 筛选后端：启用分类筛选功能
    filter_backends = [DjangoFilterBackend]
    # 筛选字段：支持按category_id筛选（对应URL参数 ?category=1）
    filterset_fields = ['category']

    def get_permissions(self):
        """
        动态权限控制（核心修正：缩进改为类内部方法）
        - 发布/编辑/删除：需登录（IsAuthenticated）
        - 查看列表/单篇：匿名可访问（AllowAny）
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """发布文章时，自动关联当前登录用户为作者（核心逻辑保留）"""
        serializer.save(author=self.request.user)