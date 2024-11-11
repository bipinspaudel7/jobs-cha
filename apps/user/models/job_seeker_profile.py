from django.db import models
from .user import User  

class JobSeekerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=255)
