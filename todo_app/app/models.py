from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=80)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item
