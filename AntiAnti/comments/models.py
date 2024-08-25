from django.db import models
from django.utils import timezone


class Comment(models.Model):
    input = models.TextField('')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.input
