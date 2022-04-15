from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

buildings = {"Block A", "Block B", "Block C", "Block D"} 

def home(request, id):
    return render(request, 'home.html', {"buildings": buildings})

def room(request):
    return render(request, 'room.html')