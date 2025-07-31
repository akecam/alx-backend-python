from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


