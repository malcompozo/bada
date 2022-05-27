from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
# methods for accessing permissions
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
            
        stuff_permissions = bool(request.user and request.user.is_staff)
        return stuff_permissions

class IsContactPermisions(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
            
        stuff_permissions = bool(request.user and request.user.is_staff)
        return stuff_permissions
