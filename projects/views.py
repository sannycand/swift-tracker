from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MemberSerializer, LogSerializer
from .models import Member, Log


class ProjectMemberAPI(viewsets.ViewSet):
    
    def user_projects(self, *args, **kwargs):
        projects = Member.objects.filter(worker=self.request.user)
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

