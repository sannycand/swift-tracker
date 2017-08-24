from django.utils import timezone

from rest_framework import serializers

from accounts.serializers import UserSerializer
from accounts.models import User

from .models import Project, Member, Company, Log


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class AddMemberSerializer(serializers.ModelSerializer):
    worker_data = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = "__all__"

    def get_worker_data(self, obj):
        worker = User.objects.get(id=obj.worker.id)
        return UserSerializer(worker).data

class ProjectSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    owner =  UserSerializer()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_members(self, obj):
        members_id = Member.objects.filter(project=obj).values_list('worker_id', flat=True)
        users = User.objects.filter(id__in=members_id)
        return UserSerializer(users, many=True).data


class MemberSerializer(serializers.ModelSerializer):
    worker = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Member
        fields = "__all__"

            
class LogSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = "__all__"

    def get_project(self, instance):
        return ProjectSerializer(instance.member.project).data

    def create(self, validated_data):       
        return Log.objects.create(
                        member=validated_data.get('member'),
                        start_time=timezone.now(),
                        description=validated_data.get('description')
                    )

    def update(self, instance, validated_data):        
        instance.end_time = timezone.now()
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance    
