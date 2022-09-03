from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    This class verify if an user has permissions to modify an user
    """

    def has_object_permission(self, request, view, obj):
        """
        This method check out if a user can modify, delete or update another user

        Returns:
            A boolean value that give us if a user can do an action
        """

        if(not request.method in permissions.SAFE_METHODS and obj.id==request.user.id
            or request.user.is_superuser):
            return True

        return False
