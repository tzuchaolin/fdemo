from django.db import models
from django.utils import timezone


class Product(models.Model):
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(blank=True, default=0)

    created_at = models.DateTimeField('created at', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True, auto_now_add=False)

