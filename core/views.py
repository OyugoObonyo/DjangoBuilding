from django.db.models import Q
from django.shortcuts import render
from buildings.models import Building


def home(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''
    # icontains isn't case sensitive whereas conatins is case_sensitive
    buildings = Building.objects.filter(
        Q(location__icontains=q) |
        Q(name__icontains=q) |
        Q(owner__username__icontains=q)
    )
    return render(request, 'home.html', {"buildings": buildings})