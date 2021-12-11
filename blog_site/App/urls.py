from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ,name="index"),
    path("blog", views.blog, name="blog"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("", views.base, name="base"),
    path("post/<str:var>", views.post, name="post"), 
]
