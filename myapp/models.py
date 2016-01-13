from django.db import models

class ItemModel(models.Model):
    name = models.CharField('Name', max_length=255, blank=True)
    unit_price = models.DecimalField('UnitPrice', max_digits=10, decimal_places=0)
