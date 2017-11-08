from django import forms

class EventForm(forms.Form):
  name = forms.CharField(label='Event name', max_length=100)
  start_time = forms.DateTimeField(label='Start time')
  end_time = forms.DateTimeField(label='End time')
  description = forms.CharField(widget=forms.Textarea)
  