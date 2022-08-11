from dealer.models import Dealer, DealerProfile, DealerCar
from rest_framework import serializers
from car.serializers import CarSerializer


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
    # car = serializers.StringRelatedField()
    # car = CarSerializer(read_only=True)
    # tracks = TrackSerializer(many=True)

    class Meta:
        model = DealerCar
        fields = [
            'car',
            'dealer',
            'price',
            'count',
        ]


class DealerProfileSerializer(serializers.ModelSerializer):
    cars = DealerCarSerializer(many=True, source='dealercar_set', read_only=True)

    class Meta:
        model = DealerProfile
        fields = [
            'pk',
            'name',
            'date_created',
            'description',
            'cars',
        ]
