from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Job, Bid, GeoLocation, Notification, Wallet, Transactions

# Auth Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'pk',
            'url',
            'username',
            'password',
            'confirm_password',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
        ]

        # def create(self, validated_data):
        #     user = User(
        #         email=validated_data["email"],
        #         username=validated_data["username"]
        #     )
        #     user.set_password(validated_data["password"])
        #     user.save()
        #     return user


# Job Serializer
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'description',
            'status',
            'employer'
        ]


# Bids Serializer

class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = [
            'id',
            'user',
            'title',
            'job',
            'timestamp',
            'date'
        ]


class GeolocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocation
        fields = [
            'id',
            'name',
            'latitude',
            'longitude'
        ]


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            'id',
            'topic',
            'message'
        ]


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = [
            'title',
            'user',
            'job',
            'bid',
            'date',
            'status',
            'description'
        ]


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = [

            'id',
            'name',
            'time',
            'amount'
        ]
