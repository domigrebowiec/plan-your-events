from django.contrib import admin

from .models import Event, EventParticipant, Person

class EventAdmin(admin.ModelAdmin):
  fields = ['name', 'start_time', 'end_time', 'description']
class EventParticipantAdmin(admin.ModelAdmin):
  fields = ['event', 'person']

admin.site.register(Event, EventAdmin)
admin.site.register(EventParticipant, EventParticipantAdmin)
admin.site.register(Person)
