from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="Home"),
   
]