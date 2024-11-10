from django.db import models

class User(models.Model):
    USER_TYPES = [
        ('JobSeeker', 'Job Seeker'),
        ('Employer', 'Employer'),
    ]
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class JobSeekerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=255)

class EmployerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    website = models.URLField()
