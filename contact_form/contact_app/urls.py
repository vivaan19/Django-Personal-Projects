from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('submit', views.submit, name="submit")
]
