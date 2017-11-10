from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Address(models.Model):
  street = models.CharField(max_length=50)
  street_nbr = models.IntegerField(default=0)
  house_nbr = models.IntegerField(default=0)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Place(models.Model):
  name = models.CharField(max_length=50)
  address = models.ForeignKey(Address)

class Event(models.Model):
  name = models.CharField(max_length=50, blank=False)
  start_time = models.DateTimeField('start time', blank=False)
  end_time = models.DateTimeField('end time', blank=False)
  #place = models.ForeignKey(Place)
  description = models.TextField(default='', blank=True)
  create_date = models.DateTimeField('create date', default=timezone.now)
  mod_date = models.DateTimeField('modification date', default=timezone.now)
  def __str__(self):
    return self.name

class EventParticipant(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(User)
  create_date = models.DateTimeField('create date', default=timezone.now)
  def __str__(self):
    return self.event.name + " " + self.user.first_name