from django.db import models
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

class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  #address = models.ForeignKey(Address)
  def __str__(self):
    return self.email

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
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  create_date = models.DateTimeField('create date', default=timezone.now)