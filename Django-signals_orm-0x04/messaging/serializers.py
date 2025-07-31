from rest_framework import serializers
from .models import Message, MessageHistory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MessageHistorySerializer(serializers.ModelSerializer):
    # message_history = MessageHistory(many=True, read_only=True)

    class Meta:
        model = MessageHistory
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    message_history = MessageHistorySerializer(many=True, read_only=True)


    class Meta:
        model = Message
        fields = "__all__"

    def perform_update(self, serializer):
        serializer.save(edited=True)
