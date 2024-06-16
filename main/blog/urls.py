from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # URLs for Category model
    path('api/v1/category/', CategoryListView.as_view(), name='category-list'),
    path('api/v1/category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('api/v1/category/<int:pk>/', CategoryAPIDetail.as_view(), name='category-detail'),
    path('api/v1/teacher/', TeacherListView.as_view(), name='teacher-list'),
    path('api/v1/teacher/create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('api/v1/teacher/<int:pk>/', TeacherAPIDetail.as_view(), name='teacher-detail'),
    # URLs for CategoryTeacher model

    # URLs for Liked model
    path('api/v1/liked/', LikedListView.as_view(), name='liked-list'),
    path('api/v1/liked/create/', LikedCreateView.as_view(), name='liked-create'),
    path('api/v1/liked/<int:pk>/', LikedAPIDetail.as_view(), name='liked-detail'),

    # URLs for Article model
    path('api/v1/article/', ArticleListView.as_view(), name='article-list'),
    path('api/v1/article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('api/v1/article/<int:pk>/', ArticleAPIDetail.as_view(), name='article-detail'),

    # URLs for Words model
    path('api/v1/words/', WordsListView.as_view(), name='words-list'),
    path('api/v1/words/create/', WordsCreateView.as_view(), name='words-create'),
    path('api/v1/words/<int:pk>/', WordsAPIDetail.as_view(), name='words-detail'),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
