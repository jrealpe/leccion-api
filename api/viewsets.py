from rest_framework import viewsets
from api import serializers
from api.models import *


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = serializers.BusSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
