from django.utils.translation import ugettext as _
from rest_framework import serializers
from api import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name')


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bus
        fields = ('id', 'name', 'n_seat')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ('id', 'city_source', 'city_goal', 'seat', 'price', 'identification')
