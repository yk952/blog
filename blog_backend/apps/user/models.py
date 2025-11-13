from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """扩展Django内置User模型，添加头像字段"""
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name=_('用户头像'),
        null=True,
        blank=True,
        help_text=_('可选，上传用户头像图片')
    )

    # 重写groups和user_permissions字段，指定唯一related_name解决冲突
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',  # 自定义反向关联名
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',  # 自定义反向关联名
        related_query_name='custom_user_permission',
    )

    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')

    def __str__(self):
        return self.username