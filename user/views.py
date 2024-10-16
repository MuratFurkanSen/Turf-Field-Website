from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, UserLoginForm


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/')

    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    return redirect('/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')