from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from user.forms import UserRegistrationForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            context = {'form': form, 'user': request.user}
            return render(request, 'home.html', context)
    else:
        form = UserRegistrationForm()

        context = {'form': form, 'user': request.user}
        return render(request, 'home.html', context)