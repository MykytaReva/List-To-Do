from django.db import models
from datetime import datetime
from todo.model_choices import Status

class CreatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Task(CreatedModel):
    td = models.CharField(max_length=50)
    td_description = models.CharField(max_length=600)
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.STATUS_ACTIVE
    )
