from dealer.models import Dealer, DealerProfile, DealerCar
from showroom.models import ShowroomProfile, ShowroomCar
from dealer.models import TransactionSellToShowroom
from rest_framework import serializers
from django.db import transaction
from decimal import Decimal


class DealerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Dealer
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = Dealer(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both password do not match'
            })


class DealerCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerCar
        fields = [
            'pk',
            'car',
            'dealer',
            'price',
            'count',
        ]


class DealerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerProfile
        fields = [
            'pk',
            'title',
            'date_created',
            'description',
            'cars',
            'balance',
        ]


class TransactionSellToShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSellToShowroom
        fields = [
            'pk',
            'car',
            'showroom',
            'dealer',
            'count',
            'price',
        ]

    # def create(self, validated_data):
    #     with transaction.atomic():
    #         # reduce count of car from dealer
    #         dealer_id = validated_data['dealer'].pk
    #         print(validated_data['dealer'].pk)
    #
    #         dealer_car = validated_data['car'].pk
    #         print(validated_data['car'].pk)
    #
    #         car_dealer = DealerCar.objects.get(dealer=dealer_id, car=dealer_car)
    #         car_dealer.count -= validated_data['count']
    #         car_dealer.save()
    #
    #         # increase balance to dealer
    #         dealer_id = validated_data['dealer'].pk
    #         dealer_ins = DealerProfile.objects.get(id=dealer_id)
    #         dealer_ins.balance += validated_data['price'] * validated_data['count']
    #         dealer_ins.save()
    #
    #         # reduce balance to showroom_profile
    #         showroom_id = validated_data['showroom'].pk
    #         showroom_inst = ShowroomProfile.objects.get(pk=showroom_id)
    #         showroom_inst.balance -= validated_data['price'] * validated_data['count']
    #         showroom_inst.save()
    #
    #         # add data to showroom_car
    #         sh_car_inst = ShowroomCar.objects.create(
    #             car=validated_data['car'],
    #             showroom=validated_data['showroom'],
    #             price=validated_data['price'] + (validated_data['price'] * Decimal(0.1)),
    #             count=validated_data['count'],
    #             dealer=validated_data['dealer']
    #         )
    #         sh_car_inst.save()
    #     return super(TransactionSellToShowroomSerializer, self).create(validated_data)
