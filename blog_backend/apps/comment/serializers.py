from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """评论序列化器"""
    username = serializers.CharField(source='user.username', read_only=True)  # 显示用户名

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'username', 'content', 'created_at']
        read_only_fields = ['user']  # 用户由后端自动填充