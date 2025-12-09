from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.showMain, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('movies/', views.movie_list, name='movie_list'),
    path('log/<int:movie_id>/', views.add_watched_movie, name='add_watched_movie'),
    path('profile/', views.profile_view, name='profile'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
