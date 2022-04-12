from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name="Blog-index"),
    path('article-<str:slug>/', article, name="article")
]