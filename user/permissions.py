from rest_framework.permissions import BasePermission

class CanViewDeletedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("user.can_view_deleted_user")