from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Airport)
admin.site.register(models.FlightDetails)
admin.site.register(models.Booking)
admin.site.register(models.Passenger)
admin.site.register(models.Employee)
