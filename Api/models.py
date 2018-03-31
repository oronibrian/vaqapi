# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=30)
    category = models.CharField(max_length=200, blank=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    time_posted = models.DateTimeField(auto_now_add=True)

    @property
    def owner(self):
        return self.employer

    def __str__(self):
        return self.title


class Bid(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    job = models.ForeignKey(Job)
    date = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    topic = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.topic


class GeoLocation(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __str__(self):
        return self.name


TRASACTION_TYPES = (
    ('Deposit', 'deposit'),
    ('Pay', 'pay'),
    ('Withdraw', 'withdraw'),

)


class Transactions(models.Model):
    name = models.CharField(
        max_length=10, choices=TRASACTION_TYPES, default='deposit')
    time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


WALLET_STATUS = (
    ('Paid', 'paid'),
    ('Not Paid', 'nonpaid'),
)


class Wallet(models.Model):
    """docstring for Wallet"""
    title = models.CharField(max_length=120)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    job = models.ForeignKey(Job)
    bid = models.ForeignKey(Bid)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=WALLET_STATUS, default='nonpaid')
    description = models.CharField(max_length=255, blank=True)
    transactions = models.ForeignKey(Transactions, default=1)

    def __str__(self):
        return self.job.title
