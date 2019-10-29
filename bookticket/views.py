from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
list_booking_id = [i for i in range(0, 300)]


def index(request):
    airport = Airport.objects.all()
    stuff_for_frontend = {"airport": airport}
    return render(request, "index.html", stuff_for_frontend)


def signIn(request):
    from_airport = request.POST['from']
    to_airport = request.POST['to']
    request.session['from_airport'] = from_airport
    request.session['to_airport'] = to_airport

    return render(request, "sign_in.html")


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
        from_ = Airport.objects.get(name=from_airport)
        to_ = Airport.objects.get(name=to_airport)
        for number in list_booking_id:
            try:
                if Booking.objects.get(booking_id=number):
                    continue
            except Booking.DoesNotExist:
                booking = Booking(booking_id=number, confirmation="No")
                booking.save()
                break
        try:
            if Passenger.objects.get(passport_no=passport):
                return HttpResponse("registerd already")
        except Passenger.DoesNotExist:
            p = Passenger(name=name, passport_no=passport, email=email, password=password, from_airport=from_,
                          to_airport=to_, flight_id=0, booking_id=booking.booking_id)
            p.save()
    return HttpResponseRedirect('mainpage/')


def main_page(request):

    return render(request, "mainpage.html")
