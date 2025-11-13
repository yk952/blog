from django.db import models
from django.conf import settings  # 新增：导入settings
from apps.article.models import Article


class Comment(models.Model):
    """评论模型"""
    content = models.TextField(verbose_name="评论内容")
    # 关联文章：当文章被删除时，关联的评论也会被删除
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="关联文章"
    )
    # 关联用户：使用settings.AUTH_USER_MODEL引用用户模型（关键修改）
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 改为引用settings中的用户模型
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="评论用户"
    )
    # 自动记录评论创建时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间"
    )

    def __str__(self):
        """返回评论的简短描述"""
        return f"{self.user.username} 评论了 《{self.article.title}》: {self.content[:20]}..."

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ["-created_time"]