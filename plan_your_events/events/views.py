from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Event, EventParticipant, Person
#laluna123
def index(request):
  all_events = Event.objects.order_by('-start_date')
  context = {
    'all_events': all_events,
  }
  return render(request, 'events/index.html', context)

def form(request):
  return render(request, 'events/form.html', {})

def addnew(request):
  try:
    event = Event.objects.get(name=request.POST['name'])
  except Event.DoesNotExist:
    event = Event(name=request.POST['name'], 
      start_date=request.POST['start_date'], 
      end_date=request.POST['end_date'], 
      create_date=timezone.now(), mod_date=timezone.now())
    event.save()
  all_events = Event.objects.order_by('-start_date')
  return redirect('events:index')

def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  try:
    participants = EventParticipant.objects.filter(event__id=event.id)
  except EventParticipant.DoesNotExist:
    participants = None
  return render(request, 'events/detail.html', {'event': event, 'participants': participants})

def signup(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  try:
    person = Person.objects.get(email=request.POST['email'])
  except Person.DoesNotExist:
    person = Person(first_name=request.POST['first_name'], 
      last_name=request.POST['last_name'], email = request.POST['email'])
    person.save()
  participant = EventParticipant(event=event, person=person, create_date=timezone.now())
  participant.save()
  return redirect('events:detail', event_id=event_id)