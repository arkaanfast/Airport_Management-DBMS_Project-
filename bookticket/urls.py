from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signIn/', views.signIn, name='signin'),
    path('register/', views.register, name='register'),
    path('passenger/', views.passenger, name='passenger'),
    path('passenger/signinagain/', views.signinagain),
    path('finalsignin/', views.finalsignin, name='signinagain'),
    path('mainpage/', views.main_page, name='mainpage'),
    path('finalsignin/register/', views.register),
    path('userpage/<int:pk>/', views.userpage, name='userpage'),
]
