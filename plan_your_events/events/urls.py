from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
  url(r'^$', views.events, name = 'events'),
  # ex: /register
  url(r'^register/$', views.register, name = 'register'),
  # ex: /login_view
  url(r'^login/$', views.login_view, name = 'login_view'),
  url(r'^logout/$', views.logout_view, name = 'logout_view'),
  # ex: /events/5/
  url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^addnew/$', views.addnew, name='addnew'),
  # ex: /events/5/signup
  url(r'^(?P<event_id>[0-9]+)/signup/$', views.signup, name='signup'),
]