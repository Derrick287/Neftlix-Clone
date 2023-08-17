from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.registerPage, name='signup'),
    path('profile/', views.userProfile, name='profile'),
    path('movie-list/', views.movieList, name='movie-list'),
    path('movie-details/', views.movieDetails, name='movie-details'),
]
