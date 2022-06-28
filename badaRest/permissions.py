from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
# methods for accessing permissions
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'GET':
            return True
            
        stuff_permissions = bool(request.user and request.user.is_staff)
        return stuff_permissions

