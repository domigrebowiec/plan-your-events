from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from .forms import LoginForm, RegistrationForm

def register(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      User.objects.create_user(username=form.cleaned_data['username'],
                  password=form.cleaned_data['password2'],
                  email=form.cleaned_data['email'])
      messages.success(request, 'You are successfully registered.')
      return redirect('events:events')
  messages.error(request, 'Error during registration.')
  return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
  form = LoginForm()
  error_message = ""
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, 'You are successfully logged in.')
        return redirect('events:events')
      else:
        messages.error(request, 'Error: Username or password are incorrect.')
  return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('events:events')

