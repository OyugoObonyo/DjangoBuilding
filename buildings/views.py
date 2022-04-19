from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import AddBuildingForm


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