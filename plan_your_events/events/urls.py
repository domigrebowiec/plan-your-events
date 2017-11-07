from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  # ex: /events/5/
  url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^form/$', views.form, name='form'),
  url(r'^addnew/$', views.addnew, name='addnew'),
  # ex: /events/5/signup
  url(r'^(?P<event_id>[0-9]+)/signup/$', views.signup, name='signup'),
]