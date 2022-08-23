from showroom.models import Showroom, ShowroomCar, ShowroomProfile
from rest_framework import serializers
from customer.models import CustomerCar, CustomerProfile
from showroom.models import TransactionSellToCustomer
from django.db import transaction
from django_countries.serializer_fields import CountryField


class ShowroomSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Showroom
        fields = [
            'pk',
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
        read_only_fields = ['pk']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = Showroom(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class ShowroomCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomCar
        fields = [
            'pk',
            'car',
            'showroom',
            'dealer',
            'count',
            'price',
        ]


class ShowroomProfileSerializer(serializers.ModelSerializer):
    location = CountryField()
    
    class Meta:
        model = ShowroomProfile
        fields = [
            'pk',
            'name',
            'location',
            'showroom_query',
            'balance',
            'cars',
        ]


class TransactionSellToCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSellToCustomer
        fields = [
            'pk',
            'car',
            'customer',
            'showroom',
            'price',
            'count',
        ]


