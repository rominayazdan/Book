from rest_framework.permissions import BasePermission
from rest_framework import permissions
from user.serializers import RegisterUserSerializer


class CanViewDeletedUser(BasePermission):
    def has_permission(self, request, view):

        return request.user.has_perm("user.can_view_deleted_user")



