from django.db import models

# Create your models here.
from django.db import models

class Reminder(models.Model):
    REMINDER_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reminder_type} - {self.date} {self.time}"
