
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutme', views.aboutme, name="about"),
    path('contact', views.contact, name="contact"),
]
