from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_number = models.IntegerField(null=False)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    departure_time = models.TimeField('departure time')
    arrival_time = models.TimeField('arrival time')
    departure_date = models.DateField('departure date')
    arrival_date = models.DateField('arrival date')
