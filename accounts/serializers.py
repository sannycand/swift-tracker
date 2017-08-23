from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Invitation


class SignupSerializer(serializers.ModelSerializer):
    """ signup serializer
    """
    password = serializers.CharField(write_only=True, required=True)
    key = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'gender',
                'birthday',
                'password',
                'key'
            ]

    def validate(self, data):
        invitation = Invitation.objects.filter(key=data.get('key'), is_used=False)
        if not invitation.exists():
            raise serializers.ValidationError("Invalid invitation key")

        return data

    def create(self, validated_data):
        invitation = Invitation.objects.get(key=validated_data['key'])
        position = invitation.position
        email = invitation.email

        user = User(
                email=email,
                username=email,
                position=position,
                first_name=validated_data.get('first_name'),
                last_name=validated_data.get('last_name'),
                gender=validated_data.get('gender'),
                birthday=validated_data.get('birthday')
            )

        if position == 'management':
            user.is_admin = True

        user.set_password(validated_data['password'])
        user.save()

        invitation.is_used = True
        invitation.save()
        Invitation.objects.filter(email=email, is_used=False).delete()

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


class UserSerializer(serializers.ModelSerializer):
    """ user serializer
    """
    class Meta:
        model = User
        fields = "__all__"


class InvitationSerializer(serializers.ModelSerializer):
    """ invitation serializer
    """
    email = serializers.EmailField(
            validators=[UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already exist!"
        )])

    class Meta:
        model = Invitation
        fields = "__all__"

    def create(self, validated_data):
        return Invitation.objects.create(**validated_data)
