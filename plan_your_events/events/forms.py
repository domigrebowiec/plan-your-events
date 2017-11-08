from django import forms
from django.utils.translation import ugettext_lazy as _

class EventForm(forms.Form):
  name = forms.CharField(label=_('Event name'), max_length=100)
  start_time = forms.DateTimeField(label='Start time')
  end_time = forms.DateTimeField(label='End time')
  description = forms.CharField(widget=forms.Textarea)
