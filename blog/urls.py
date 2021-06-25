from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_new, name='blog_new'),
    path('blog/edit/<int:pk>/', views.blog_edit, name='blog_edit'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
]
