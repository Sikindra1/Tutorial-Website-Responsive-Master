from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("videos/", views.videos, name="videos"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.userLogin, name="userlogin"),
    path("register/", views.userCreate, name="userCreate"),
    path("logout/", views.userLogout, name="userLogout"),
]
