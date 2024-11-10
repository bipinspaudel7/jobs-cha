from django.db import models

# create your models here

# User model
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

# Job Seeker Profile model
class JobSeekerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=255)

# Employer Profile model
class EmployerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    website = models.URLField()

# Admin Panel model
class AdminPanel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_management = models.BooleanField(default=False)
    job_management = models.BooleanField(default=False)
    analytics_access = models.BooleanField(default=False)

# Job Listings model
class JobListing(models.Model):
    job_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

# Job Applications model
class JobApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    resume_snapshot = models.CharField(max_length=255)

# Notifications model
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# Premium Features model
class PremiumFeature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_type = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


