from django.db import models
from apps.user.models.user import User

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
