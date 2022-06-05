from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.landingpage, name='landingPage'),
    path('team/', views.teamPage, name='team'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('profile/<str:username>', views.viewProfile.as_view(), name='viewProfile'),
    path('resetPassword', views.resetPassword.as_view(), name='resetPassword'),
    path('logout', views.Logout, name='Logout'),
    path('uploadbarcode', views.uploadBarcode.as_view(), name="uploadBarcode"),
    path('search/', views.search, name='search'),
    path('rent/<str:barcode>', views.rent, name='rent'),
<<<<<<< HEAD
    path('home', views.homePage, name='homePage'),
=======
    path('returnbook/<str:barcode>/<str:prn>', views.return_book_superuser, name='returnBook')
>>>>>>> cec122c72b578b2be20439c12461472900d10311
]
