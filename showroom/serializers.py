from showroom.models import Showroom, ShowroomCar, ShowroomProfile
from rest_framework import serializers
from dealer.models import DealerCar


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

    def create(self, validated_data):
        # get dealer id
        dealer_id = validated_data['dealer'].pk
        # get car_dealer
        car_dealer = DealerCar.objects.get(dealer=dealer_id)
        # reduce car to related dealer
        car_dealer.count -= validated_data['count']
        car_dealer.save()
        return super(ShowroomCarSerializer, self).create(validated_data)


class ShowroomProfileSerializer(serializers.ModelSerializer):
    cars = ShowroomCarSerializer(many=True, source='showroomcar_set', read_only=True)

    class Meta:
        model = ShowroomProfile
        fields = [
            'pk',
            'name',
            # 'location',
            'car_description',
            'balance',
            'cars',
        ]
