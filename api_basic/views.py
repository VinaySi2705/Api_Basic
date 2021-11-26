from .models import Article
from .serializers import ArticleSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

#using ViewSet

class ArticleViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    #jwt authentications
    authentication_classes = [JWTAuthentication]

    #get api
    def list(self,request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset,many=True)
        return Response(serializer.data)

    #post api
    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #retrieve  api
    def retrieve(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    #put api
    def update(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #patch api
    def partial_update(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #delete api
    def destroy(self,request,pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
