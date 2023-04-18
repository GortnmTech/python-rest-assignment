from django.shortcuts import render

# Create your views here.
# Views and Responses
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (# CreateAPIView,
                                     # ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

# Django Tools
from django.contrib.auth import get_user_model

# Local Imports
from posts.serializers import PostSerializer
from posts.models import Post


class CreatePostAPI(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        data = request.data
        author = request.user  # get_user_model().objects.get(pk=data.get('author'))
        if 'image' not in request.FILES or 'caption' not in data :
            return Response(status=status.HTTP_400_BAD_REQUEST,data={"message" :"Required fields are missing"})
        post = Post(
            author=author,
            image=request.FILES["image"],
            caption=data.get('caption'),
        )
        post.save()
        return Response(status=status.HTTP_201_CREATED,data={'message': "post created successfully"})


class POSTAPI(APIView):
    def delete(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        user = request.user
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message":"successfully deleted"})

        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})

    def get(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        user = request.user
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            postt=PostSerializer(post)
            return Response(status=status.HTTP_200_OK, data=postt.data)

        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})




class GetPostAPI(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPI(DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LikePostAPI(APIView):
    def get(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        user = request.user#get_user_model().objects.get(pk=kwargs['req_user_pk'])
        try:
            post = Post.objects.get(pk=kwargs['post_pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            if user in post.likes.all():
                post.likes.remove(user)
                return Response(status=status.HTTP_200_OK,data={"messages": "Post unliked"})

            else:
                post.likes.add(user)

                return Response(status=status.HTTP_200_OK, data={"messages": "Post liked"})

        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})

