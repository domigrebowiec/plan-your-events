from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .forms import EventForm
from .models import Event, EventParticipant
#laluna123

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
      messages.success(request, 'You added new event.')
      return redirect('events:events')
  else:
    form = EventForm()
  return render(request, 'events/form.html', {'form': form})

def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  participants = EventParticipant.objects.filter(event__id=event.id)
  return render(request, 'events/detail.html', {'event': event, 'participants': participants})

@login_required(login_url='/accounts/login/')
def signup(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  try:
    event_p = EventParticipant.objects.get(event__id=event.id,user__id=request.user.id)
    messages.error(request, 'You are already signup for this event!')
    participants = EventParticipant.objects.filter(event__id=event.id)
    return redirect('events:detail', event.id)
  except EventParticipant.DoesNotExist:
    participant = EventParticipant(event=event, user=request.user)
    participant.save()
    messages.success(request, 'You are successfully signup for this event.')
  return redirect('events:detail', event.id)
