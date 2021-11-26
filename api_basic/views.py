from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

#using ViewSet

class ArticleViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self,request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # article=Article.objects.get(pk=pk)
        # data = request.data
        # article.title = data.get('title',article.title)
        # article.author = data.get('author',article.author)
        # article.email = data.get('email',article.email)
        # article.created_date = data.get('created_date',article.created_date)
        # article.content = data.get('content',article.content)
        # article.save()
        # serializer = ArticleSerializer(article)
        # return Response(serializer.data)

    def destroy(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#using model ViewSet

class ArticleModelViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#using generics
class ArticleList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
