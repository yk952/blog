from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    """注册序列化器"""
    password = serializers.CharField(write_only=True, min_length=6, label='密码')

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # 密码加密存储
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """登录序列化器"""
    username = serializers.CharField(label='用户名')
    password = serializers.CharField(label='密码', write_only=True)

    def validate(self, data):
        # 验证用户名密码
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError('用户名或密码错误')
        return {'user': user}