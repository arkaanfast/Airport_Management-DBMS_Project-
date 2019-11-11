from django.db import models

# Create your models here.


class Airport(models.Model):

    airport_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FlightDetails(models.Model):

    flight_id = models.IntegerField(primary_key=True)
    flight_name = models.CharField(max_length=50)
    from_airport = models.ForeignKey(Airport, related_name="from_airport_id", on_delete=models.CASCADE)
    time_arrival = models.DateTimeField()
    time_departure = models.DateTimeField()
    to_airport = models.ForeignKey(Airport, related_name="to_airport_id", on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.flight_name


class Booking(models.Model):

    booking_id = models.IntegerField(primary_key=True)
    confirmation = models.CharField(max_length=4)


class Passenger(models.Model):

    from_airport = models.ForeignKey(Airport, related_name="from_airport", on_delete=models.CASCADE)
    to_airport = models.ForeignKey(Airport, related_name="to_airport", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    flight = models.ForeignKey(FlightDetails, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):

    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    salary = models.FloatField()
    duty = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.emp_name



