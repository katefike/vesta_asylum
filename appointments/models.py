'''
Remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
'''
import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

class Appointments(models.Model):
    question_text = models.CharField(max_length=200)
    post_date = models.DateTimeField("time posted")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="post_date",
        description="Posted recently?",
    )
    def was_posted_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.post_date <= now
