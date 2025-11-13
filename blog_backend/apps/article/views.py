from rest_framework import viewsets
from .models import Article  # 导入Article模型
from .serializers import ArticleSerializer  # 导入上面定义的序列化器
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图集：基于ModelViewSet实现完整的CRUD操作
    自动支持：
    - GET /articles/：列表查询（list）
    - GET /articles/{id}/：单篇查询（retrieve）
    - POST /articles/：发布文章（create）
    - PUT /articles/{id}/：修改文章（update）
    - DELETE /articles/{id}/：删除文章（destroy）
    """
    # 查询集：指定需要操作的模型数据（这里是所有文章）
    queryset = Article.objects.all()
    # 序列化器：指定使用的序列化器
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 发布文章时，将当前登录用户设置为作者
        serializer.save(author=self.request.user)

def get_permissions(self):
    if self.action in ['create', 'update', 'partial_update', 'destroy']:
        # 发布/修改文章需要登录
        return [permissions.IsAuthenticated()]
        # 查看文章允许匿名
    return [permissions.AllowAny()]