from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    performer = models.ForeignKey(User, blank=True, null=True)

    taken = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
       return 'Task: ' + self.name