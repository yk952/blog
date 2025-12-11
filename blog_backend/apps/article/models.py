from django.db import models
from django.conf import settings  # 用于关联用户模型
from django.contrib.auth.models import User

class Category(models.Model):
    """文章分类模型"""
    name = models.CharField(
        max_length=100,
        unique=True,  # 确保分类名唯一，避免重复
        verbose_name="分类名称"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )

    class Meta:
        verbose_name = "分类"  # 后台显示的单数名称
        verbose_name_plural = verbose_name  # 后台显示的复数名称（与单数一致）
        ordering = ["-create_time"]  # 默认按创建时间倒序排列

    def __str__(self):
        # 显示分类名称，方便在后台和调试时识别
        return self.name


class Article(models.Model):
    """文章模型"""
    title = models.CharField(
        max_length=200,  # 标题长度限制
        verbose_name="文章标题"
    )
    content = models.TextField(  # 长文本字段，适合存储文章内容
        verbose_name="文章内容"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 关联Django内置用户模型（支持自定义用户模型）
        on_delete=models.CASCADE,  # 若作者被删除，关联的文章也会被删除
        related_name="articles",  # 反向查询：用户.articles 可获取该用户的所有文章
        verbose_name="作者"
    )
    category = models.ForeignKey(
        Category,  # 关联分类模型
        on_delete=models.CASCADE,  # 若分类被删除，关联的文章也会被删除
        related_name="articles",  # 反向查询：分类.articles 可获取该分类下的所有文章
        verbose_name="所属分类"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,  # 首次创建时自动记录当前时间（不可修改）
        verbose_name="创建时间"
    )
    update_time = models.DateTimeField(
        auto_now=True,  # 每次保存时自动更新为当前时间
        verbose_name="更新时间"
    )
    is_published = models.BooleanField(
        default=False,  # 默认未发布
        verbose_name="是否发布"
    )

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]  # 默认按创建时间倒序排列（最新的在前）

    def __str__(self):
        # 显示文章标题，方便识别
        return self.title