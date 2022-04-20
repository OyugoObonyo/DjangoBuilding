from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from buildings.models import Building


def home(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''
    buildings = Building.objects.filter(location__icontains=q)
    return render(request, 'home.html', {"buildings": buildings})