from django.db import models

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
  name = models.CharField(max_length=50)
  start_date = models.DateTimeField('start date')
  end_date = models.DateTimeField('end date')
  #place = models.ForeignKey(Place)
  create_date = models.DateTimeField('create date')
  mod_date = models.DateTimeField('modification date')
  def __str__(self):
    return self.name

class EventParticipant(models.Model):
  event = models.ForeignKey(Event)
  person = models.ForeignKey(Person)
  create_date = models.DateTimeField('create date')