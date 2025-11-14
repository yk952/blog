from django.urls import path,include

urlpatterns=[
    path('auth/',include('dj_rest_auth.urls')),  #用户认证，直接使用别人写好的库
    path('auth/registration/',include('dj_rest_auth.registration.urls')), #注册
]