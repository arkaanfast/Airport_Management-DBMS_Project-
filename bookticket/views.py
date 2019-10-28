from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):

    airport = Airport.objects.all()
    stuff_for_frontend = {"airport": airport}
    return render(request, "index.html", stuff_for_frontend)


def signin(request):

    return render(request, "index.html")
