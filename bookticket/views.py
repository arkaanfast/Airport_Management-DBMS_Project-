from django.shortcuts import render, HttpResponse, reverse, redirect
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


def signinagain(request):
    return render(request, "sign_in.html")


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
    return redirect('signinagain/')


def main_page(request):

    flights_set = set()
    from_airport = Airport.objects.get(name=request.session.get("from_airport"))
    to_airport = Airport.objects.get(name=request.session.get("to_airport"))
    a = from_airport.from_airport_id.all()
    b = to_airport.to_airport_id.all()
    for flights in a:
        for flight in b:
            if flights.to_airport == flight.to_airport:
                flights_set.add(flights)
    stuff_for_front_end = {"flights": flights_set}
    return render(request, "mainpage.html", stuff_for_front_end)


def finalsignin(request):

    email = request.POST['email']
    password = request.POST['password']
    from_ = request.session.get('from_airport')
    to_ = request.session.get('to_airport')
    try:
        if Passenger.objects.get(email=email):
            p = Passenger.objects.get(email=email)
            if p.password == password:
                request.session['from_airport'] = from_
                request.session['to_airport'] = to_
                request.session['passenger'] = p.email
                return redirect(reverse('mainpage'))
            else:
                return HttpResponse("Password is incorect")
    except Passenger.DoesNotExist:
        return HttpResponse("<a href='register/'>Click to register</a>")


def userpage(request, pk):
    p = Passenger.objects.get(email=request.session.get('passenger'))
    p.flight_id = pk
    p.save()
    flight_to_render = FlightDetails.objects.get(flight_id=pk)
    context = {"flight": flight_to_render}
    return render(request, 'userpage.html', context)


