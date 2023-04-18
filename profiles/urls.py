from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),

    path('details/',UserAPIView.as_view(),name="user"),
    path('register/',CreateUserAPI.as_view(),name="register_user"),
    path('followers/',Userfollowers_listAPIView.as_view(),name="userfollowers"),
    path('followings/',Userfollowing_listAPIView.as_view(),name="userfollowings"),
    path('posts/',Userposts_listSerializerAPIView.as_view(),name="userposts"),

    path('follow/',followAPIView.as_view(),name="follow"),
    path('unfollow/',unfollowAPIView.as_view(),name="unfollow"),

    #path('api/userdetails/',GetUserAPI.as_view(),name="user_details")

]
