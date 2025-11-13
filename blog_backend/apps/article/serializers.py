from rest_framework import serializers
from .models import Article  # 导入Article模型


class ArticleSerializer(serializers.ModelSerializer):
    """文章序列化器：将Article模型转换为JSON格式"""
    
    class Meta:
        model = Article  # 关联的模型
        # 指定需要返回的字段（根据需求调整，这里包含id、title、content）
        fields = ['id', 'title', 'content']
        # 若需要包含模型所有字段，可简写为 fields = '__all__'
        # 若需要排除某些字段，可使用 exclude = ['字段名']