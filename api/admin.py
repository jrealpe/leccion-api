from django.contrib import admin
from api import models

# Register your models here.

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_seat')


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('city_source', 'city_goal', 'seat', 'price', 'identification')

