from django.urls import path
from posts.views import CreatePostAPI, GetPostAPI,UpdatePostAPI, DeletePostAPI,LikePostAPI

urlpatterns = [

    path('create/',CreatePostAPI.as_view(),name='create_post_api'),

    path('get/<int:pk>/',GetPostAPI.as_view(),name='get_post_api'),

    path('update/<int:pk>/',UpdatePostAPI.as_view(),name='update_post_api'),

    path('delete/<int:pk>/',DeletePostAPI.as_view(),name='delete_post_api'),

    path('like/<int:req_user_pk>/<int:post_pk>/',LikePostAPI.as_view(),name='like_post_api'),


]