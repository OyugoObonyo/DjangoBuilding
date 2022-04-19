from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from buildings.models import Building


def home(request):
    buildings = Building.objects.all()
    return render(request, 'home.html', {"buildings": buildings})