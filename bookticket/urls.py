from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signIn/', views.signIn, name='signIn'),
    path('register/', views.register, name='register'),
    path('passenger/', views.passenger, name='passenger'),
]
