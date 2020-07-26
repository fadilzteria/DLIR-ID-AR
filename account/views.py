from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .forms import RegisterForm

def index(request):
    pass

def logins(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            context = {
                'title': "Kitab Ulama",
            }
            return redirect('/', context)
    else:
        form = LoginForm()
    context = {
        'title': "Login | Kitab Ulama",
        'form': form,
    }
    return render(request, 'account/login.html', context)

# @login_required
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            context = {
                'title': "Kitab Ulama",
            }
            return redirect('/', context)
    else:
        form = RegisterForm()
    context = {
        'title': "Registrasi | Kitab Ulama",
        'form': form,
    }
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
