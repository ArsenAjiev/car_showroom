from core.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
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
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })
