from django.db import models
from .user import EmployerProfile, JobSeekerProfile

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

class JobApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    resume_snapshot = models.CharField(max_length=255)
