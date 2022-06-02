from django.shortcuts import render

from .models import * #Flight, Airport

# Create your views here.

def index(request):
    return render(request, 'flights/index.html',{
        "flights" : Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(id = flight_id)
    return render(request, 'flights/flight.html',{
        "flight": flight # you can use 'Flight.objects.get(id = flight_id)' but I flight variable and use it. 
    })