from django.contrib import admin
from django.urls import path
# from Django_Tutorials.Sample import Sample_app
from . import views
urlpatterns = [
    path("", views.index, name="Sample_app"),  # this is home page. 
    path("about", views.about, name="Sample_app"),
    path("contact", views.contact, name="Sample_app"),
    path("services", views.services, name="Sample_app"),
    # path("connect", views.connect, name="Sample_app"),
    # path("", views.extend_1, name="Sample_app"),
]
