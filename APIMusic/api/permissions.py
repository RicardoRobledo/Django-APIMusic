"""
This module define permissions about what we can
do in our api
"""


__author__ = "Ricardo Robledo"
__version__ = "0.1"


from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
