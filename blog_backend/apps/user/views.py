from rest_framework import viewsets, status,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer

class UserViewSet(viewsets.GenericViewSet):
    """用户注册/登录视图集"""
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='register',authentication_classes=[],permission_classes=[permissions.AllowAny])
    def register(self, request):
        """注册接口（仅允许POST方法）"""
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'msg': '注册成功',
                'token': token.key,
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """登录接口（返回Token）"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # 创建/获取用户Token
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id
        })