from rest_framework.permissions import BasePermission

class BelongsToUser(BasePermission):
    def has_permission(self, request, view):
        pass