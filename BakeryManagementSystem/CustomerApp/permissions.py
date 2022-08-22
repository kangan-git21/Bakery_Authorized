from rest_framework import permissions


class IsOwnerLogged(permissions.BasePermission):
    """Allow only owner to read"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return False






