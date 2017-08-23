from django.contrib.auth import login, logout

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer, LoginSerializer, UserSerializer, InvitationSerializer
from .models import User
from .mixins import EmailMixin


class UserAPI(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def signup(self, *args, **kwargs):
        serializer = SignupSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 

    def login(self, *args, **kwargs):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            login(self.request, serializer.user)

            return Response(serializer.data, status=204)
        return Response(serializer.errors, status=400) 
        
    def logout(self, *args, **kwargs):
        logout(self.request)
        return Response(status=204)


class AuthUserAPI(viewsets.ViewSet):

    def user(self, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data, status=200)


class InvitationAPI(EmailMixin, viewsets.ViewSet):
    
    def invite(self, *args, **kwargs):
        if self.request.user.is_admin:
            serializer = InvitationSerializer(data=self.request.data)
            if serializer.is_valid():
                instance = serializer.save()

                url = self.request.build_absolute_uri('/') + 'signup-' + instance.key + '/'
                self.user_invite(instance.email, url)

                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response(status=401)
