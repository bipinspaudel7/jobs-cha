from django.db import models
from .user import User

class PremiumFeature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_type = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
