from django.contrib import admin

from .models import Event, EventParticipant

class EventAdmin(admin.ModelAdmin):
  fields = ['name', 'start_time', 'end_time', 'description']
class EventParticipantAdmin(admin.ModelAdmin):
  fields = ['event', 'user']

admin.site.register(Event, EventAdmin)
admin.site.register(EventParticipant, EventParticipantAdmin)
