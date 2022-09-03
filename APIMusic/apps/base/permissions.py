from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if(not request.method in permissions.SAFE_METHODS and obj.id==request.user.id
            or request.user.is_superuser):
            return True

        return False
