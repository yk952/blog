from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'', UserViewSet,basename='user')

urlpatterns=[
    path('auth/',include('dj_rest_auth.urls')),  #用户认证，直接使用别人写好的库
    path('',include(router.urls)),
]