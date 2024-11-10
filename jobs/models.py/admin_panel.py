from django.db import models

class AdminPanel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_management = models.BooleanField(default=False)
    job_management = models.BooleanField(default=False)
    analytics_access = models.BooleanField(default=False)
