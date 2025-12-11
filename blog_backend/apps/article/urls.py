from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import ArticleViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter



def article(request):
    return HttpResponse("Hello, world. You're at the article index.")
router=DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path("test/", article ),
    path('', include(router.urls)),
]
