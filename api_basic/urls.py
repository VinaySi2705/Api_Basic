from django.urls import path,include
from .views import (ArticleList,
                    ArticleDetail,
                    ArticleViewSet,
                    ArticleModelViewset)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                        TokenObtainPairView,
                        TokenRefreshView,
                        TokenVerifyView,
)

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
router.register('articleview',ArticleModelViewset,basename='articleview')
urlpatterns = [
   path('viewset/',include(router.urls)),
   path('article/',ArticleList.as_view()),
   path('article/<int:pk>/',ArticleDetail.as_view()),

   #jwt authentication
   path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
   path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
   path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
