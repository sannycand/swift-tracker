from django.utils import timezone

from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Project, Member, Company, Log


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Project
        fields = "__all__"

            
class MemberSerializer(serializers.ModelSerializer):
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
