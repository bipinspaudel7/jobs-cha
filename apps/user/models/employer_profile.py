from django.db import models
from .user import User

class EmployerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    website = models.URLField()
