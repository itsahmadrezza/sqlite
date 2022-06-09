from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })



def flight(request, flight_id):
    flight = Flight.objects.get(id = flight_id)
    passengers = flight.passengers.all()
    return render(request, 'flights/flight.html',{
        "flight": flight,
        "passenger": passengers
    })