from django.dispatch import receiver
from .models import Message, Notification
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model



User = get_user_model()

@receiver(post_save, sender=Message)
def trigger_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)