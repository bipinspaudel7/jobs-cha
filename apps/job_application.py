from django.db import models
from .job_listing import JobListing
from .user.user import JobSeekerProfile

class JobApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    resume_snapshot = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.job_seeker} - {self.job.title}"
