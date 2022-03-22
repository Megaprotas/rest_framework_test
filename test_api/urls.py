from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test_api import views

router = DefaultRouter()
router.register('main_viewset', views.SecondViewSet, basename='main-viewset')
router.register('profile', views.UserProfileViewset)
router.register('feed', views.UserProfileFeedViewset)

urlpatterns = [
    path('main_apiview/', views.FirstView.as_view()),
    path('login', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]