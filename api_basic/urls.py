from django.urls import path,include
from .views import (ArticleList,
                    ArticleDetail,
                    ArticleViewSet,
                    ArticleModelViewset)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
router.register('articleview',ArticleModelViewset,basename='articleview')
urlpatterns = [
   path('viewset/',include(router.urls)),
   path('article/',ArticleList.as_view()),
   path('article/<int:pk>/',ArticleDetail.as_view()),
]
