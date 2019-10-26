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

    def __str__(self):
        return self.flight_name
