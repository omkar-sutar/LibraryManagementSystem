from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.landingpage, name='landingPage'),
    path('home/', views.homePage, name='homePage'),
    path('team/', views.teamPage, name='team'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='signup'),
    path('profile/<str:username>', views.viewProfile.as_view(), name='viewProfile'),
    path('resetPassword', views.resetPassword.as_view(), name='resetPassword'),
    path('logout', views.Logout, name='logout'),
    path('uploadbarcode', views.uploadBarcode.as_view(), name="uploadBarcode"),
    path('search/', views.search, name='search'),
    path('rent/<str:barcode>', views.rent, name='rent'),
    path('returnbook/<str:barcode>/<str:prn>', views.return_book_superuser, name='returnBook')
]
