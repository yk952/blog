from rest_framework import serializers
from .models import Article, Category  # 导入关联模型


class ArticleSerializer(serializers.ModelSerializer):
    """文章序列化器：适配视图集自动填充author、支持分类ID传递"""
    # 处理分类外键：接收分类ID，返回时也显示ID（适配前端v-model绑定的category ID）
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),  # 校验分类ID是否存在（避免无效ID）
        allow_null=True,  # 允许分类为空（若业务允许文章无分类，可开启）
        required=False    # 非必填（根据业务调整，若强制选分类则设为True）
    )

    class Meta:
        model = Article  # 关联Article模型
        # 字段列表：与前端提交的字段对齐，author/create_time只读（后端自动填充）
        fields = ['id', 'title', 'content', 'create_time', 'author', 'category']
        # 只读字段：前端无需传递，后端自动生成/填充
        read_only_fields = ['author', 'create_time']
        # 可选：若需要自定义字段验证（比如标题长度），可添加字段校验
        extra_kwargs = {
            'title': {'max_length': 200, 'min_length': 2},  # 标题长度限制
            'content': {'required': True}  # 内容必填（后端兜底校验）
        }


class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器：与前端Category类型对齐"""
    class Meta:
        model = Category
        # 字段与前端categories.ts中的Category接口（id/name/create_time）完全对齐
        fields = ["id", "name", "create_time"]
        # 分类创建时间只读（自动生成）
        read_only_fields = ['create_time']