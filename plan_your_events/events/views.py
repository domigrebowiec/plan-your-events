from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import EventForm
from .models import Event, EventParticipant, Person
#laluna123

def events(request):
  all_events = Event.objects.order_by('-start_time')
  context = {
    'all_events': all_events,
  }
  return render(request, 'events/events.html', context)

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
  participant = EventParticipant(event=event, person=person)
  participant.save()
  return redirect('events:detail', event_id=event_id)