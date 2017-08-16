from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer
from .models import User


class UserAPI(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def signup(self, *args, **kwargs):
        serializer = SignupSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 