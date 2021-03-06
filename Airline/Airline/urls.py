"""Airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import routers
# from flights.views import CreateFlight, ListFlights, DetailFlight
from flights import views


# router = routers.DefaultRouter()
# router.register('create', CreateFlight)
# router.register('flights', ListFlights)


urlpatterns = [
    url(r'^flights/$', views.list_flights),
    url(r'^flights/(?P<flight_id>[0-9]+)$', views.flight_detail),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# url(r'^create/', views.CreateFlight.as_view()),
# url(r'^flights/(?P<flight_id>[0-9]+)', views.DetailFlight.as_view()),
# url(r'^flights/', views.ListFlights.as_view()),
