from rest_framework import serializers
from .models import UserProfile, SocialLink, AboutText, Experience, Project, Writing

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'profession', 'shortBio']

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['github', 'instagram', 'linkedin', 'telegram']

class AboutTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutText
        fields = ['aboutText']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['dateRange', 'title', 'description', 'technologies']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'imageUrl', 'technologies']

class WritingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writing
        fields = ['imageUrl', 'date', 'title', 'link']
