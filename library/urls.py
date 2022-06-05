from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.landingpage, name='landingPage'),
    path('home/', views.homePage, name='homePage'),
    path('team/', views.teamPage, name='team'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('profile/<str:username>', views.viewProfile.as_view(), name='viewProfile'),
    path('resetPassword', views.resetPassword.as_view(), name='resetPassword'),
    path('logout', views.Logout, name='Logout'),
    path('uploadbarcode', views.uploadBarcode.as_view(),name="uploadBarcode"),
    path('search/<str:query>',views.search,name='search'),

]