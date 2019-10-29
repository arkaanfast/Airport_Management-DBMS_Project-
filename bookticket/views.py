from django.shortcuts import render, HttpResponse
from random import randint
from .models import *
# Create your views here.


def index(request):

    airport = Airport.objects.all()
    stuff_for_frontend = {"airport": airport}
    return render(request, "index.html", stuff_for_frontend)


def signin(request):

    from_airport = request.POST['from']
    to_airport = request.POST['to']
    request.session['from_airport'] = from_airport
    request.session['to_airport'] = to_airport

    return render(request, "signin.html")


def register(request):

    return render(request, "register.html")


def passenger(request):

    if request.method == "POST":
        from_airport = request.session.get('from_airport')
        to_airport = request.session.get('to_airport')
        name = request.POST['first']
        passport = request.POST['passport']
        email = request.POST['email']
        password = request.POST['pass']
        booking_id = randint(1, 100)
        booking = Booking(booking_id=booking_id, confirmation="No")
        booking.save()
        from_ = Airport.objects.get(name=from_airport)
        to_ = Airport.objects.get(name=to_airport)
        p = Passenger(name=name, passport_no=passport, email=email, password=password, from_airport=from_,
                      to_airport=to_, flight_id=0, booking_id=booking.booking_id)
        p.save()
    return HttpResponse("hello")
