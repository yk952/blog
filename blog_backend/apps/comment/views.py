from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # 权限控制：列表/详情匿名可看，创建需登录，编辑/删除仅本人可操作
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    # 创建评论时自动关联当前用户
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 筛选：按文章ID查询评论
    def get_queryset(self):
        article_id = self.request.query_params.get('article_id')
        if article_id:
            return Comment.objects.filter(article_id=article_id).order_by('-create_time')
        return Comment.objects.all().order_by('-create_time')