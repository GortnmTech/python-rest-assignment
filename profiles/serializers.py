from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models import Post

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'full_name', 'username', 'birthday', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('full_name', 'username', 'profile_pic', 'bio', 'gender',
                'ph_number','account_type', 'followers_count', 'following_count', 'posts_count')


class Userfollowers_listSerializer(serializers.ModelSerializer):
    followers_list = serializers.SerializerMethodField()

    def get_followers_list(self, profile):
        return UserSerializer(profile.followers_list(), many=True).data
    class Meta:
        model=get_user_model()
        fields=('followers_list',)

class Userfollowing_listSerializer(serializers.ModelSerializer):
    following_list = serializers.SerializerMethodField()
    def get_following_list(self, profile):
        return UserSerializer(profile.following_list(), many=True).data
    class Meta:
        model=get_user_model()
        fields=('following_list',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('author','image','posted_time','caption','likes')

class Userposts_listSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    def get_posts(self, profile):
        return PostSerializer(profile.posts(), many=True).data
    class Meta:
        model=get_user_model()
        fields=('posts',)