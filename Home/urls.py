from django.contrib import admin
from django.urls import path, include
from Home import views

app_name = 'Home'

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('Signup', views.SignUp, name="SignUp"),
    path('Login', views.Login, name="Login"),
    path('Logout', views.Logout, name="Logout"),
]
