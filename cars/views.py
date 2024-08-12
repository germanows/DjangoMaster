from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car

def cars_view(request):
    return HttpResponse("Meus carros :)")

# Create your views here.
