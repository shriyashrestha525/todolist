from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page
from accounts.views import register_page

urlpatterns = [
    
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register")
]