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
