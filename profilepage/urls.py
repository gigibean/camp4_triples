from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('mr/', views.mr, name='mr'),
    path('songs/', views.songs, name='songs'),
    path('likes/', views.likes, name='likes'),
    path('followings/', views.followings, name='followings'),
    path('followers/', views.followers, name='followers'),
    path('comments/', views.comments, name='comments'),
]