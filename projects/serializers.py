from rest_framework import serializers

from .models import Project, Member, Company


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

