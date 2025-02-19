from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to allow owners to edit their own profile. """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
