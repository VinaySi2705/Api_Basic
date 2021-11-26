from django.urls import path,include
from .views import ArticleViewSet

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                        TokenObtainPairView,
                        TokenRefreshView,
                        TokenVerifyView,
)

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
urlpatterns = [
   path('',include(router.urls)),
   #jwt authentication
   path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
   path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
   path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
