from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def login_user(request): 
    """
    
    handles user login
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # This query doesn't return None if its empty hence we're wrapping 
            # it in a try-except block 
            user = User.objects.get(username=username)
        except:
            return HttpResponse(f"A user called {username} doesn't exist")
        # this will return None in case authenticate fails          
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        return HttpResponse("Username or password is incorrect")
    return render(request, 'authentication/login_form.html')

def logout_user(request):
    """
    
    handles user logout
    """
    logout(request)
    return redirect('home')

def register_user(request):
    """
    
    handles user registration
    """
    form = UserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # don't commit user object to DB but immediately capture and store created item
            user = form.save(commit=False)
            # you can perform whatever action here on the frozen user object
            user.save()
            return redirect('login')
    return render(request, 'authentication/register_form.html', context)