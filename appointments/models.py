'''
Remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
'''
from datetime import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class AppointmentPosts(models.Model):
    appointment = models.CharField(max_length=132)
    post_time = models.DateTimeField("time posted", auto_now_add=True)

    def __str__(self):
        return self.appointment
    
    def latest_post_time_delta():
        latest_post = AppointmentPosts.objects.latest('post_time')
        now = timezone.now()
        delta = now - latest_post.post_time
        return delta

    # @admin.display(
    #     boolean=True,
    #     ordering="post_time",
    #     description="Posted recently?",
    # )
    # def was_posted_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.post_time <= now
