from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView



from .forms import SignupForm, LoginForm

# Create your views here.



def home(request):
    return render(request, 'core/home.html')



def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/rooms/')
        else:
            return render(request, 'core/signup.html', {'form': form})
    else:
        return render(request, 'core/signup.html', {'form': form})



def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/rooms/')
            else:
                return render(request, 'core/login.html', {'form': form})
        else:
            return render(request, 'core/login.html', {'form': form})
    else:
        return render(request, 'core/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('/')

