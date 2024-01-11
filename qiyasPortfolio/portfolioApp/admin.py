from django.contrib import admin
from .models import UserProfile, SocialLink, AboutText, Experience, Project, Writing

models = [UserProfile, SocialLink, AboutText, Experience, Project, Writing]

for model in models:
    admin.site.register(model)
