# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from .serializers import UserSerializer, JobSerializer, BidSerializer,UserLoginSerializer, NotificationSerializer, GeolocationSerializer, WalletSerializer, TransactionsSerializer
from .models import Job, Bid, Notification, GeoLocation, Wallet, Transactions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    look_up_field = 'pk'
    permission_classes =[AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class userLoginViewSet(APIView):
    permission_classes =[AllowAny]
    queryset = User.objects.all()

    serializer_class = UserLoginSerializer


    def post(self,request,*args,**kwargs):
        data= request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data= serializer.data
            return Response(new_data,status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



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
