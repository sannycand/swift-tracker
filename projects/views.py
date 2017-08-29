from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer

from .serializers import (
                MemberSerializer,
                LogSerializer, 
                ProjectSerializer,  
                AddMemberSerializer                
                )
from .models import Member, Log, Project


class ProjectMemberAPI(viewsets.ViewSet):
    
    def user_projects(self, *args, **kwargs):
        projects = Member.objects.filter(worker=self.request.user, project__is_archived=False)
        return Response(MemberSerializer(projects, many=True).data, status=200)


class LogAPI(viewsets.ViewSet):
    
    def start_log(self, *args, **kwargs):
        member = get_object_or_404(Member, worker=self.request.user, project=kwargs['project_id'])

        data = self.request.data
        data['member'] = member.id

        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def stop_log(self, *args, **kwargs):
        log = get_object_or_404(Log, id=self.request.data.get('id'), member__worker=self.request.user)
        
        serializer = LogSerializer(log, data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def current_log(self, *args, **kwargs):
        logs = Log.objects.filter(member__worker=self.request.user, end_time=None).order_by('-id')
        
        if logs:
            return Response(LogSerializer(logs.first()).data, status=200)
        return Response(status=204)


class ProjectAPI(viewsets.ViewSet):
    
    def projects(self, *args, **kwargs):        
        return Response(ProjectSerializer(
            Project.objects.all(), many=True).data, status=200)

    def users(self, *args, **kwargs):
        users = User.objects.exclude(id=self.request.user.id)
        project = get_object_or_404(Project, id=kwargs['project_id'])
        users_id = Member.objects.filter(project=project).values_list('worker_id', flat=True)
        
        return Response(UserSerializer(users.exclude(id__in=users_id), many=True).data, status=200)
        
    def add_member(self, *args, **kwargs):
        serializer = AddMemberSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def add_project(self, *args, **kwargs):
        data = self.request.data
        data['owner'] = self.request.user.id

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update_project(self, *args, **kwargs):
        project = get_object_or_404(Project, id=kwargs['project_id'])

        serializer = ProjectSerializer(project, data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
