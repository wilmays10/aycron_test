from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    number = models.CharField(_('Number'), max_length = 30, blank = True)
    street = models.CharField(_('Address'), max_length = 100, blank = True)
    zipcode = models.CharField(_('ZIP code'), max_length = 5, blank = True)
    state = models.CharField(_('State'), max_length = 100, blank = True)
    county = models.CharField(_('County'), max_length = 100, blank = True)

    def __str__(self):
        result = f'{self.street} - {self.number}' if self.street else self.id
        return result


class Warehouse(models.Model):
    code = models.PositiveIntegerField(_('Code'), unique=True)
    name = models.CharField(_('Name'), max_length=255)
    address = models.ForeignKey(Address, related_name='warehouses',
                               on_delete=models.SET_NULL, null=True,
                               blank=True)

    def __str__(self):
        return f'{self.code} - {self.name}'
