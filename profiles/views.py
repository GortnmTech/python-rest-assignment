from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .serializers import *
from .models import User



class UserAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class Userfollowers_listAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Userfollowers_listSerializer

    def get_object(self):
        return self.request.user

class Userfollowing_listAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Userfollowing_listSerializer

    def get_object(self):
        return self.request.user

class Userposts_listSerializerAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Userposts_listSerializer

    def get_object(self):
        return self.request.user


class followAPIView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        #print(request.data['username'])
        if 'username' in request.data:
            user = User.objects.filter(username=request.data['username']).first()
            if user:
                if user == request.user:
                    return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Can't Follow himself"})
                elif user not in request.user.following.all():
                    request.user.following.add(user)
                    user.followers.add(request.user)
                    return Response(status=status.HTTP_200_OK, data={'message': 'Following user'})
                else:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Already Following user'})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'user not found'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'need username to follow'})


class unfollowAPIView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticated,)
        # print(request.data['username'])
        if 'username' in request.data:
            user = User.objects.filter(username=request.data['username']).first()
            print(request.user.following.all())
            if user:
                if user == request.user:
                    return Response(status=status.HTTP_200_OK, data={'message': "Can't Follow or unfollow himself"})
                elif user in request.user.following.all():
                    request.user.following.remove(user)
                    user.followers.remove(request.user)
                    return Response(status=status.HTTP_200_OK, data={'message': 'unFollowing user'})
                else:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Already unFollowing user'})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'user not found'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'need username to unfollow'})



class CreateUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.full_name = user.full_name.title()
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_201_CREATED, data={"Success": True})
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, data=serializer.errors)


