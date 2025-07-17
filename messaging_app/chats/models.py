from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid


# Create your models here.
class User(AbstractUser):

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)



class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="conversations"
    )




class Message(models.Model):

    message_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages'
    )
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages'
    )