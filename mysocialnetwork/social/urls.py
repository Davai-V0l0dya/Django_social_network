from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('create_post/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
