from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from buildings.models import Building, Review, Tenant
from .forms import AddBuildingForm, UpdateBuildingForm


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_building(request, id):
    """
    
    delete_bulding deletes a building from the db
    """

    building = Building.objects.get(id=id)
    building.delete()
    return redirect('home')

@login_required(login_url='login')
def show_reviews(request, id):
    """
    
    show_reviews shows all reviews for a particular building
    """
    
    building = Building.objects.get(id=id)
    building_reviews = building.review_set.all()
    tenants = building.tenants.all()
    if request.method == "POST":
        review = Review.objects.create(
            body = request.POST.get("review"),
            owner=request.user,
            building=building
        )
        return redirect(request.META.get('HTTP_REFERER', '/'))    
    context = {"building": building, "building_reviews": building_reviews, "tenants": tenants}
    return render(request, 'buildings/show_all_reviews.html', context)

@login_required(login_url='login')
def move_in_building(request, id):
    """
    
    move_in_building allows users to move into a partcular building
    """
    building = Building.objects.get(id=id)
    tenant = Tenant(name=request.user)
    # instead of saving twice, i.e tenant.save and building.save, consider how to
    # implement 'through' in the database models
    tenant.save()
    building.tenants.add(tenant)
    building.save()
    return HttpResponse("You are now a tenant...")

@login_required(login_url='login')
def view_tenants(request, id):
    """
    
    view_tenants allows users to view all tenants of a particular building
    """
    
    
    building = Building.objects.get(id=id)
    building_tenants = building.tenants.all()
    context = {"building": building, "building_tenants": building_tenants} 
    return render(request, 'buildings/show_all_tenants.html', context)