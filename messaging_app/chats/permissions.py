from rest_framework import permissions


class IsParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only participants to access the conversation
        return obj.participants.filter(user_id=request.user.user_id).exists()