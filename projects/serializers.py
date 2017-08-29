from django.utils import timezone

from rest_framework import serializers

from accounts.serializers import UserSerializer
from accounts.models import User

from .models import Project, Member, Log


class AddMemberSerializer(serializers.ModelSerializer):
    worker_data = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = "__all__"

    def get_worker_data(self, obj):
        return UserSerializer(obj.worker).data


class ProjectSerializer(serializers.ModelSerializer):
    owner_data = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_owner_data(self, obj):
        return UserSerializer(obj.owner).data

    def get_members(self, obj):
        members_id = Member.objects.filter(project=obj).values_list('worker_id', flat=True)
        users = User.objects.filter(id__in=members_id)
        return UserSerializer(users, many=True).data

    def create(self, validated_data):
        project = Project.objects.filter(name__iexact=validated_data.get('name'))
        if project.exists():
            raise serializers.ValidationError("Project name already exist!")
        
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if instance.name != name:
            project = Project.objects.filter(name__iexact=name)
            if project.exists():
                raise serializers.ValidationError("Project name already exist!")

        instance.name = name
        instance.is_archived = validated_data.get('is_archived', instance.is_archived)
        instance.save()

        return instance


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
