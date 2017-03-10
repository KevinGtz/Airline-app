from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flight
from .serializers import FlightSerializer
# Create your views here.


# Search Flights
# def index(request):
#     pass


# Show a list of Flights
@api_view(['GET', 'POST'])
def list_flights(request, format=None):
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def flight_detail(request, flight_id, format=None):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ListFlights(APIView):
#
#     def get(self, request):
#         flights = Flight.objects.all()
#         serializer = FlightSerializer(flights, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = FlightSerializer(data=request.data)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class DetailFlight(APIView):
#
#     def get(self, request, flight_id):
#         flight = get_object_or_404(Flight, pk=flight_id)
#         serializer = FlightSerializer(flight)
#         return Response(serializer.data)


# Show Flight Details
# def flight_details(request, flight_id):
#     flight = get_object_or_404(Flight, pk=flight_id)
#     return render(request, 'flights/flight_detail.html', {'flight': flight})

# class CreateFlight(viewsets.ModelViewSet):
#
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer


#     return Flight.objects.all()

# Create Flights -*- (KLG 03/07/17) I think this need to be only in the admin page -*-
# def create_flights(request):
#     pass
