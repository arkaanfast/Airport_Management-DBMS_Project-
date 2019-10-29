from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('passenger/', views.passenger, name='passenger'),
]
