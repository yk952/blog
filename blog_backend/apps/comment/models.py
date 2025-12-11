from django.db import models
from django.conf import settings
from apps.article.models import Article


class Comment(models.Model):
    """评论模型（无冗余字段，命名统一）"""
    content = models.TextField(
        verbose_name="评论内容",
        blank=False,  # 显式声明内容不能为空
        null=False
    )
    # 关联文章：评论必须绑定文章，文章删除则评论也删除
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="关联文章",
        null=False
    )
    # 关联用户：评论必须绑定用户，用户删除则评论也删除
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="评论用户",
        null=False
    )
    # 统一用 created_at（符合Django/DRF 命名习惯：*_at 表示时间戳）
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    # 最后更新时间
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间"
    )

    def __str__(self):
        """返回评论简短描述（增加容错性）"""
        article_title = self.article.title if self.article else "未知文章"
        username = self.user.username if self.user else "未知用户"
        return f"{username} 评论《{article_title}》: {self.content[:20]}..."

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ["-created_at"]  # 同步改为 created_at
        # 新增索引：优化按文章+创建时间筛选的查询性能
        indexes = [
            models.Index(fields=["article", "-created_at"]),
            models.Index(fields=["user"]),
        ]