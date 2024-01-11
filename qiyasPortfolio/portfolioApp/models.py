from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    shortBio = models.TextField()

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    github = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)

    def __str__(self):
        return f"Social Links of {self.userProfile.name}"

class AboutText(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    aboutText = models.TextField()

    def __str__(self):
        return f"About Text of {self.userProfile.name}"

class Experience(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dateRange = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.JSONField()

    def __str__(self):
        return f"{self.title} at {self.userProfile.name}"

class Project(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl = models.URLField(max_length=200)
    technologies = models.JSONField()

    def __str__(self):
        return self.title

class Writing(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    imageUrl = models.URLField(max_length=200)
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
