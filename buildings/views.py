from multiprocessing import context
from django.shortcuts import render, redirect

from buildings.models import Building
from .forms import AddBuildingForm, UpdateBuildingForm


def add_building(request):
    """

    add_building adds a building to the db
    """
    
    form = AddBuildingForm()
    if request.method == 'POST':
        form = AddBuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'buildings/create_building_form.html', context)


def update_building(request, id):
    """
    
    update_building updates an existing building 
    """

    building = Building.objects.get(id=id)
    form = UpdateBuildingForm(instance=building)
    if request.method == "POST":
        form = UpdateBuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'buildings/update_building_form.html', context)


def delete_building(request, id):
    """
    
    delete_bulding deletes a building from the db
    """

    building = Building.objects.get(id=id)
    building.delete()
    return redirect('home')