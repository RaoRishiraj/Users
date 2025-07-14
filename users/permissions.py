from rest_framework.permissions import BasePermission

class IsRoleAdministrator(BasePermission):

    def has_permission(self, request, _view):
        return request.user.is_authenticated and request.user.role == 'administrator'