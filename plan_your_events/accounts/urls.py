from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
  # ex: /register
  url(r'^register/$', views.register, name = 'register'),
  # ex: /login_view
  url(r'^login/$', views.login_view, name = 'login_view'),
  url(r'^logout/$', views.logout_view, name = 'logout_view'),
]