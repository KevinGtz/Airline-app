from django.conf.urls import url

from . import views

app_name = 'flights'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.list_flights, name='list_flights'),
    url(r'^(?P<flight_id>[0-9]+)/$', views.flight_details, name='flight_details'),
]
