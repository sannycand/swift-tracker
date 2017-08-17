from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MemberSerializer
from .models import Member


class ProjectMemberAPI(viewsets.ViewSet):
    
    def user_projects(self, *args, **kwargs):
        projects = Member.objects.filter(worker=self.request.user)
        return Response(MemberSerializer(projects, many=True).data, status=200)
