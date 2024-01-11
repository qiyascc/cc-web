from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import UserProfile, SocialLink, AboutText, Experience, Project, Writing
from .serializers import (UserProfileSerializer, SocialLinkSerializer, 
                          AboutTextSerializer, ExperienceSerializer, 
                          ProjectSerializer, WritingSerializer)


def index(request):
    return render(request, "index.html")

def user_data_view(request):
    data = {}
    return JsonResponse(data)

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer