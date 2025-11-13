from rest_framework import serializers
from .models import Article, Category  # 导入Article模型


class ArticleSerializer(serializers.ModelSerializer):
   # 显式声明category字段，接收分类ID（PrimaryKeyRelatedField专门处理外键ID）
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),  # 指定查询集，确保ID存在
        write_only=False  # 允许读写（创建时接收ID，返回时显示ID）
    )
    
    class Meta:
        model = Article  # 关联的模型
        # 指定需要返回的字段（根据需求调整，这里包含id、title、content）
        fields = ['id', 'title', 'content', 'created_at', 'author', 'category']
        read_only_fields = ['author', 'created_at']
        # 若需要包含模型所有字段，可简写为 fields = '__all__'
        # 若需要排除某些字段，可使用 exclude = ['字段名']