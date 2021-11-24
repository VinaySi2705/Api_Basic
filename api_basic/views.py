from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import permissions

class ArticleList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
