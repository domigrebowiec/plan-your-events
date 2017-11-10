from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import EventForm, LoginForm, PersonForm, RegistrationForm
from .models import Event, EventParticipant, Person
#laluna123

def register(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      User.objects.create_user(username=form.cleaned_data['username'],
                  password=form.cleaned_data['password2'],
                  email=form.cleaned_data['email'])
      return redirect('events:events')
  return render(request, 'events/register.html', {'form':form})

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
  return render(request, 'events/login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
  logout(request)
  return redirect('events:events')

def events(request):
  all_events = Event.objects.order_by('-start_time')
  context = {
    'all_events': all_events,
  }
  return render(request, 'events/events.html', context)

#@login_required(login_url='/events/login/')
def addnew(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      try:
        event = Event.objects.get(name=form.cleaned_data['name'])
      except Event.DoesNotExist:
        event = Event(name=form.cleaned_data['name'], 
          start_time=form.cleaned_data['start_time'], 
          end_time=form.cleaned_data['end_time'], 
          description=form.cleaned_data['description'])
        event.save()
      all_events = Event.objects.order_by('-start_time')
      return redirect('events:events')
  else:
    form = EventForm()
  return render(request, 'events/form.html', {'form': form})

def detail(request, event_id, form=PersonForm()):
  event = get_object_or_404(Event, pk=event_id)
  #try:
  participants = EventParticipant.objects.filter(event__id=event.id)
  #except EventParticipant.DoesNotExist:
    #participants = None
  return render(request, 'events/detail.html', {'event': event, 'participants': participants, 'form': form})

def signup(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  if request.method == 'POST':
    form = PersonForm(request.POST)
    if form.is_valid():
      try:
        person = Person.objects.get(email=form.cleaned_data['email'])
        event_p = EventParticipant.objects.get(event__id=event.id,person__id=person.id)
        print('EventParticipant already exist')
      except Person.DoesNotExist:
        person = Person(first_name=form.cleaned_data['first_name'], 
          last_name=form.cleaned_data['last_name'], email = form.cleaned_data['email'])
        person.save()
      except EventParticipant.DoesNotExist:
        participant = EventParticipant(event=event, person=person)
        participant.save()
        print('EventParticipant saved')
      return redirect('events:detail', event_id=event.id)
  else:
    form = PersonForm()
  print('event_id', event_id)
  return render(request, 'events/detail.html', {'event_id': event.id, 'form': form})