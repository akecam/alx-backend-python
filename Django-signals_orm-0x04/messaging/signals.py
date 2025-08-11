from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Message)
def trigger_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)


@receiver(pre_save, sender=Message)
def trigger_message_history(sender, instance, raw, using, update_fields, **kwargs):
    if not raw:
        MessageHistory.objects.create(message_history_content=instance)


@receiver(post_delete, sender=User)
def delete_user(sender, instance, using, **kwargs):
    Notification.objects.get(user=instance.receiver).delete()
    MessageHistory.objects.get(edited_by=instance.receiver).delete()
    Message.objects.get(sender=instance.receiver).delete()
