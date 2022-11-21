from django.db import models

class Status(models.TextChoices):
    STATUS_ACTIVE = 'Active', 'Active'
    STATUS_COMPLETED = 'Completed', 'Completed'
