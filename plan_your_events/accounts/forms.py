from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='* Username', max_length=30)
    first_name = forms.CharField(label='First name', max_length=30, required=False)
    last_name = forms.CharField(label='Last name', max_length=30, required=False)
    email = forms.EmailField(label='* Email')
    password1 = forms.CharField(label='* Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='* Password (Again)', widget=forms.PasswordInput())

    def clean_password2(self):
      if 'password1' in self.cleaned_data:
          password1 = self.cleaned_data['password1']
          password2 = self.cleaned_data['password2']
          if password1 == password2:
              return password2
      raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
      username = self.cleaned_data['username']
      if not re.search(r'^\w+$', username): #checks if all the characters in username are in the regex. If they aren't, it returns None
          raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
      try:
          User.objects.get(username=username) #this raises an ObjectDoesNotExist exception if it doesn't find a user with that username
      except ObjectDoesNotExist:
          return username #if username doesn't exist, this is good. We can create the username
      raise forms.ValidationError('Username is already taken.')

class LoginForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  password = forms.CharField(label='Password', widget=forms.PasswordInput())