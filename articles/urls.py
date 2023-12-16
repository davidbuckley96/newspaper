from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('<str:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<str:pk>/edit/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('<str:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),


]

