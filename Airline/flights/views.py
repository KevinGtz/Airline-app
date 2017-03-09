from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flight
from .serializers import FlihgtSerializer
# Create your views here.


# Search Flights
# def index(request):
#     pass


# Show a list of Flights
class ListFlights(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlihgtSerializer(flights, many=True)
        return Response(serializer.data)


# Show Flight Details
# def flight_details(request, flight_id):
#     flight = get_object_or_404(Flight, pk=flight_id)
#     return render(request, 'flights/flight_detail.html', {'flight': flight})


# Create Flights -*- (KLG 03/07/17) I think this need to be only in the admin page -*-
# def create_flights(request):
#     pass
