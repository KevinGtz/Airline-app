from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_name = models.CharField(max_length=100, default='name of flight')
    flight_number = models.IntegerField(null=False)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.TimeField('departure time')
    arrival_time = models.TimeField('arrival time')
    departure_date = models.DateField('departure date')
    arrival_date = models.DateField('arrival date')

    def __str__(self):
        return self.flight_name

