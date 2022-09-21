from customer.models import Customer, CustomerProfile, CustomerCar
from rest_framework import serializers
from car.serializers import CarSerializer


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


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = [
            'pk',
            'title',
            'customer_query',
            'balance',
            'cars',
        ]


class CustomerCarSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)
    customer = CustomerProfileSerializer(read_only=True)

    class Meta:
        model = CustomerCar
        fields = [
            'pk',
            'car',
            'customer',
            'showroom',
            'count',
            'price',
        ]


