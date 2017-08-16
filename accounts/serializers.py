from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    """ signup serializer
    """
    email = serializers.EmailField(
            validators=[UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already exist!",
            )])
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
                'email',
                'position',
                'password'
            ]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],
            position=validated_data['position']
            )

        position = validated_data['position']
        if position == 'management':
            user.is_admin = True

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    """ login serializer
    """
    user = None

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        self.user = authenticate(email=email, password=password)
        if self.user is None or not self.user.is_active:
            raise serializers.ValidationError("Invalid email or password")

        return data

