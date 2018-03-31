# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Job, Bid, Notification, GeoLocation, Wallet, Transactions

# Register your models here.


class WalletModelAdmin(admin.ModelAdmin):
    list_display = ["date", "title", "user", "job", "bid", "status"]
    list_display_links = ["date"]
    list_filter = ["date"]

    search_fields = ["title", "status"]

    class Meta:
        model = Wallet


class BidModelAdmin(admin.ModelAdmin):
    list_display = ["date", "title", "user", "job", "timestamp"]
    list_display_links = ["date"]
    list_filter = ["date", "timestamp"]

    search_fields = ["job", "user"]

    class Meta:
        model = Bid

admin.site.register(Job)
admin.site.register(Bid, BidModelAdmin)
admin.site.register(Notification)
admin.site.register(GeoLocation)
admin.site.register(Wallet, WalletModelAdmin)
admin.site.register(Transactions)
