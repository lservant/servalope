from __future__ import unicode_literals
from django.contrib.auth.models import User
import datetime

from django.db import models

# Create your models here.

class Mailing(models.Model):
    """Represents an event"""
    name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.today)
    message = models.CharField(blank=True, max_length=100)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __unicode__(self):
        return u"Mailing"

class Guest(models.Model):
    """Represents a guest of a given mailing"""
    RSVP_CHOICES = (
        ('Y','Yes'),
        ('M','Maybe'),
        ('N','No'),
    )

    first = models.CharField(blank=True, max_length=100)
    middle = models.CharField(blank=True, max_length=100)
    last = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    mailing = models.ForeignKey(Mailing,on_delete=models.CASCADE)
    rsvp = models.CharField(choices=RSVP_CHOICES,max_length=1)

    def __unicode__(self):
        return u"Guest"
