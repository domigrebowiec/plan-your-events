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
      return redirect('events:events')
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
        return redirect('events:events')
      else:
        error_message = "Error"
  return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
  logout(request)
  return redirect('events:events')

