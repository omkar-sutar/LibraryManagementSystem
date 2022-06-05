from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.landingPage.as_view(), name='landingPage'),
    path('home', views.homePage, name='homePage'),
    path('login', views.Login.as_view(), name='Login'),
    path('register', views.register.as_view(), name='register'),
    path('profile/<str:username>', views.viewProfile.as_view(), name='viewProfile'),
    path('resetPassword', views.resetPassword.as_view(), name='resetPassword'),
    path('logout', views.Logout, name='Logout'),
    path('uploadbarcode', views.uploadBarcode.as_view(),name="uploadBarcode"),
    path('search/<str:query>',view=views.search,name='search'),
    path('rent/<str:barcode>',views.rent,name='rent'),
    path('return/<str:barcode>/<str:prn>',views.return_book_superuser),
]