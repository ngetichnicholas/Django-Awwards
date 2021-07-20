from rest_framework import serializers
from .models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'user', 'phone','address']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'posted_on','project_image','repo_link','live_link','user' ,'technologies_used']

