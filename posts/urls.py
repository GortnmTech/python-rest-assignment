from django.urls import path
from posts.views import CreatePostAPI, GetPostAPI, DeletePostAPI,LikePostAPI,POSTAPI

urlpatterns = [

    path('create/',CreatePostAPI.as_view(),name='create_post_api'),

    path('<int:pk>/',POSTAPI.as_view(),name='get_post_api'),

    #path('delete/<int:pk>/',DeletePostAPI.as_view(),name='delete_post_api'),

    path('like/<int:post_pk>/',LikePostAPI.as_view(),name='like_post_api'),


]