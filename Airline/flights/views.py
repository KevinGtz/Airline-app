from django.shortcuts import get_object_or_404, render

from .models import Flight
# Create your views here.


# Search Flights
def index(request):
    pass


# Show a list of Flights
def list_flights(request):
    latest_flights_list = Flight.objects.order_by('?')[:10]
    context = {
        'latest_flights_list': latest_flights_list
    }
    return render(request, 'flights/flights.html', context=context)


# Show Flight Details
def flight_details(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/flight_detail.html', {'flight': flight})


# Create Flights -*- (KLG 03/07/17) I think this need to be only in the admin page -*-
def create_flights(request):
    pass
