from rest_framework import serializers

from .models import Category, Teacher, Liked, Article, Words

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"




class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = "__all__"
