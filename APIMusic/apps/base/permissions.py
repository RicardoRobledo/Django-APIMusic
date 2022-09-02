from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return True if not request.method in permissions.SAFE_METHODS and obj==request.user else False
