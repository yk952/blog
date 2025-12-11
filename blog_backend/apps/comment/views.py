from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from .models import Comment
from .serializers import CommentSerializer

# ===================== 新增：自定义权限类 IsOwnerOrReadOnly =====================
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限：仅评论的所有者可编辑/删除，其他用户仅可查看
    """
    def has_object_permission(self, request, view, obj):
        # 只读请求（GET/HEAD/OPTIONS）允许所有用户
        if request.method in permissions.SAFE_METHODS:
            return True
        # 写请求（PUT/DELETE）仅允许评论的所有者（obj.user 需匹配模型字段）
        return obj.user == request.user

# ===================== 修正后的 CommentViewSet =====================
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # 基础权限：默认匿名可看（后续通过get_permissions动态覆盖）
    permission_classes = [permissions.AllowAny]

    # 动态权限控制（修正逻辑，更严谨）
    def get_permissions(self):
        """
        - create（POST）：需登录
        - update/partial_update/destroy（PUT/PATCH/DELETE）：需登录 + 是评论所有者
        - list/retrieve（GET）：匿名可访问
        """
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            # 导入自定义的IsOwnerOrReadOnly（关键！）
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        # 列表/详情：匿名可看
        return [permissions.AllowAny()]

    # 创建评论时自动关联当前登录用户（需确保Comment模型有user字段）
    def perform_create(self, serializer):
        # 补充：校验请求数据（可选，兜底前端校验）
        if not serializer.validated_data.get('content'):
            raise ValidationError({"content": "评论内容不能为空"})
        # 关联当前用户（确保Comment模型的评论者字段是user）
        serializer.save(user=self.request.user)

    # 筛选：按文章ID查询评论（增强类型校验，避免无效筛选）
    def get_queryset(self):
        queryset = Comment.objects.all().order_by('-created_at')
        # 获取并校验article_id参数
        article_id = self.request.query_params.get('article_id')
        if article_id:
            try:
                article_id = int(article_id)  # 转为数字，避免字符串筛选
                queryset = queryset.filter(article_id=article_id)
            except ValueError:
                raise ValidationError({"article_id": "文章ID必须是数字"})
        return queryset