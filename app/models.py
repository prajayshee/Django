# models.py
from django.db import models
from datetime import date, timedelta

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    due_date = models.DateField(default=date.today)
    reminder_time = models.DateTimeField(null=True, blank=True)  # New field for reminder
    priority = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
