from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Message(models.Model):
    message_id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True)
    sender = models.ForeignKey(User, models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)


class Notification(models.Model):
    notification_id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True)
    user = models.ForeignKey(User, models.CASCADE, related_name="notifications")
    message = models.ForeignKey(Message, models.CASCADE, related_name="notification")


class MessageHistory(models.Model):
    message_history_id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True)
    message_history_content = models.ForeignKey(Message, models.CASCADE, related_name="message_history")
