# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from .serializers import UserSerializer, JobSerializer, BidSerializer, NotificationSerializer, GeolocationSerializer, WalletSerializer, TransactionsSerializer
from .models import Job, Bid, Notification, GeoLocation, Wallet, Transactions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    look_up_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint For Jobs.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class BidsList(viewsets.ModelViewSet):
    """
    This view should return a list of all the Bids
    for the currently authenticated user.
    """
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    # permission_classes=(IsAuthenticated)
    # authentication_classes=(BasicAuthentication,SessionAuthentication)
    queryset = Notification.objects.all()
    look_up_field = 'pk'
    serializer_class = NotificationSerializer


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = GeoLocation.objects.all()
    serializer_class = GeolocationSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
