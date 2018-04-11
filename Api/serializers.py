from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Job, Bid, GeoLocation, Notification, Wallet, Transactions
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.views import exception_handler
from django.core.exceptions import ValidationError


# Auth Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'pk',
            'url',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff', 
        ]

    def validate(self, attrs):
        password = attrs['password']
        if len(password) < 9:
            raise serializers.ValidationError("password is too short.")
        return attrs

    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass.objects.create_user(**validated_data)
        return instance



#Login serializer
class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            
            'username',
            'password',
        ]

    def validate(self, data):
        user_obj=None
        username=data.get('username',None)
        password= data["password"]
        if not username:
            raise ValidationError('Username is empty')

        user = User.objects.filter(
                Q(username=username)
            ).distinct()

        if user.exists() and user.count()==1:
            user_obj=user.first()
        else:
            raise ValidationError('The username does not exist')
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect Credential')


        
        return data

# Job Serializer
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'status',
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
