from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.landingPage.as_view(), name='landingPage'),
    path('login', views.Login.as_view(), name='Login'),
    path('register', views.register.as_view(), name='register'),
    path('profile', views.viewProfile.as_view(), name='viewProfile'),
    path('resetPassword', views.resetPassword.as_view(), name='resetPassword'),
    path('logout', views.Logout, name='Logout'),
]