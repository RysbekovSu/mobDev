from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import Category, Teacher, Liked, Article, Words
from .serializers import CategorySerializer, TeacherSerializer, LikedSerializer, \
    ArticleSerializer, WordsSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (AllowAny,)

class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (AllowAny,)

class TeacherAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (AllowAny,)





class LikedListView(generics.ListAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
    permission_classes = (AllowAny,)

class LikedCreateView(generics.CreateAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
    permission_classes = (AllowAny,)

class LikedAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
    permission_classes = (AllowAny,)


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)

class ArticleAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)

class WordsListView(generics.ListAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    permission_classes = (AllowAny,)

class WordsCreateView(generics.CreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    permission_classes = (AllowAny,)

class WordsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    permission_classes = (AllowAny,)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
