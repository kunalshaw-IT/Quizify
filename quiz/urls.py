from django.contrib import admin
from django.urls import path, include
from quiz import views

urlpatterns = [
    path('', views.home, name='home'),
    path('question', views.question, name='question'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signupUser, name='signup'),
    path('logout', views.logoutUser, name='logout'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('login_home', views.login_home, name='login_home'),
    path('thankyou/<int:score>', views.thankyou, name='thankyou')
]