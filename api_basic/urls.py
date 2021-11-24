from django.urls import path
from .views import ArticleList

urlpatterns = [
   path('article/',ArticleList.as_view()),
]
