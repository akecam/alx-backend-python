from rest_framework import serializers
from .models import Message, Conversation
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "bio",
            "address",
            "is_admin",
        ]


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ["conversation_id", "created_at", "participants"]

    def validate(self, attrs):
        participants = self.initial_data.get("participants", [])  # type: ignore

        if len(participants) < 2:
            raise ValidationError(
                "Users must be up to 2 before starting a conversation"
            )
        return attrs


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    conversation = ConversationSerializer(read_only=True)
    sent_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Message
        fields = [
            "message_id",
            "message_body",
            "sent_at",
            "is_read",
            "sender",
            "conversation",
        ]
