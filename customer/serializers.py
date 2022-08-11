from customer.models import Customer, CustomerProfile, CustomerCar
from showroom.models import Showroom, ShowroomCar
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Customer
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

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = Customer(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class CustomerCarSerializer(serializers.ModelSerializer):
    first_car_id = serializers.PrimaryKeyRelatedField(source='car.car.car.pk', read_only=True)
    car_made = serializers.PrimaryKeyRelatedField(source='car.car.car.make', read_only=True)

    class Meta:
        model = CustomerCar
        fields = [
            'car',
            'first_car_id',
            'car_made',
            'customer',
            'showroom',
            'count',
            'price',
        ]

    def create(self, validated_data):
        # get showroom id
        showroom_id = validated_data['showroom'].pk
        # get car_dealer
        car_showroom = ShowroomCar.objects.get(showroom=showroom_id)
        # reduce car to related dealer
        car_showroom.count -= validated_data['count']
        car_showroom.save()
        return super(CustomerCarSerializer, self).create(validated_data)


class CustomerProfileSerializer(serializers.ModelSerializer):
    cars = CustomerCarSerializer(many=True, source='customercar_set')

    class Meta:
        model = CustomerProfile
        fields = [
            'pk',
            'name',
            'email',
            'balance',
            'cars',
        ]
