from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('pok/', views.pok, name="pok")
]