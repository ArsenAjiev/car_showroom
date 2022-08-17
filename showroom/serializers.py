from showroom.models import Showroom, ShowroomCar, ShowroomProfile
from rest_framework import serializers
from customer.models import CustomerCar, CustomerProfile
from showroom.models import TransactionSellToCustomer
from django.db import transaction


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
            'car',
            'showroom',
            'dealer',
            'count',
            'price',
        ]


class ShowroomProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomProfile
        fields = [
            'pk',
            'name',
            # 'location',
            'showroom_query',
            'balance',
            'cars',
        ]


class TransactionSellToCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSellToCustomer
        fields = [
            'car',
            'customer',
            'showroom',
            'price',
            'count',
        ]

    def create(self, validated_data):
        with transaction.atomic():
            # reduce count of car from showroom
            showroom_id = validated_data['showroom'].pk
            showroom_car = validated_data['car'].pk
            car_showroom = ShowroomCar.objects.get(showroom=showroom_id, car=showroom_car)
            car_showroom.count -= validated_data['count']
            car_showroom.save()

            # increase balance from showroom
            showroom_id = validated_data['showroom'].pk
            showroom_ins = ShowroomProfile.objects.get(id=showroom_id)
            showroom_ins.balance += validated_data['price'] * validated_data['count']
            showroom_ins.save()

            # reduce balance to customer_profile
            customer_id = validated_data['customer'].pk
            customer_inst = CustomerProfile.objects.get(pk=customer_id)
            customer_inst.balance -= validated_data['price'] * validated_data['count']
            customer_inst.save()

            # add data to showroom_car
            sh_car_inst = CustomerCar.objects.create(
                car=validated_data['car'],
                showroom=validated_data['showroom'],
                customer=validated_data['customer'],
                price=validated_data['price'],
                count=validated_data['count']
            )
            sh_car_inst.save()
        return super(TransactionSellToCustomerSerializer, self).create(validated_data)
