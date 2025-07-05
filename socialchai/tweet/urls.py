#  BASE_DIR = Path(__file__).resolve().parent.parent
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import Tweet
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'), 
    path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'), 
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'), 
    path('register/', views.register, name='register'), 
] 