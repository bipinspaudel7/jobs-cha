from django.db import models
from .user.user import EmployerProfile

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

    def __str__(self):
        return self.title
