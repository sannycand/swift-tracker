from django.contrib.auth import login, logout
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer, LoginSerializer, UserSerializer
from .models import User


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