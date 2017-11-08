from django import forms
from django.utils.translation import ugettext_lazy as _

class EventForm(forms.Form):
  name = forms.CharField(label=_('Event name'), max_length=100)
  start_time = forms.DateTimeField(label='Start time', widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}))
  end_time = forms.DateTimeField(label='End time', widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}))
  description = forms.CharField(widget=forms.Textarea)
