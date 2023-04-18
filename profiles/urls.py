from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),

    path('api/userdetails/',UserAPIView.as_view(),name="user"),
    path('api/registeruser/',CreateUserAPI.as_view(),name="register_user"),
    path('api/userfollowers/',Userfollowers_listAPIView.as_view(),name="userfollowers"),
    path('api/userfollowings/',Userfollowing_listAPIView.as_view(),name="userfollowings"),
    path('api/posts/',Userposts_listSerializerAPIView.as_view(),name="userposts"),

    path('api/followuser/',followAPIView.as_view(),name="follow"),
    path('api/unfollowuser/',unfollowAPIView.as_view(),name="unfollow"),

    #path('api/userdetails/',GetUserAPI.as_view(),name="user_details")

]
