from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class City(models.Model):
    name = models.CharField(_('Ciudad'), max_length=30)

    class Meta:
       verbose_name = _('Ciudad')
       verbose_name_plural = _('Ciudades')


class Bus(models.Model):
    name = models.CharField(_('Bus'), max_length=30)
    n_seat = models.PositiveSmallIntegerField(_('Número de asiento'))

    class Meta:
       verbose_name = _('Bus')
       verbose_name_plural = _('Buses')


class Ticket(models.Model):
    city_source = models.ForeignKey(
        City,
        related_name='source_tickets',
        verbose_name=_('Ciudad Origen'))
    city_goal = models.ForeignKey(
        City,
        related_name='goal_tickets',
        verbose_name=_('Ciudad Destino'))
    seat = models.PositiveSmallIntegerField(_('Número de asiento'))
    price = models.FloatField(_('Precio'))   
    identification = models.PositiveIntegerField(_('Número de cédula'))
    date_created = models.DateTimeField(_('Fecha de emisión'),auto_now_add=True)

    class Meta:
       verbose_name = _('Ticket')
       verbose_name_plural = _('Tickets')
