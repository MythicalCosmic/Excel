from django.db import models
from django.utils import timezone

class OrderStatus(models.TextChoices):
    NEW = 'NEW', 'New'
    WAITING = 'WAITING', 'Waiting'
    CANCELED = 'CANCELED', 'Canceled'


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    passport_number = models.IntegerField(null=True)
    passport_letter = models.CharField(null=True, max_length=255)
    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.NEW,
    )
    created_at = models.DateTimeField(default=timezone.now)