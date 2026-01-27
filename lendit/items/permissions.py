
from rest_framework import permissions
class ItemsGetAllowAnyCreateAuthUpdateDeleteOwner(permissions.BasePermission):
    OWNER_METHODS = (
        "update", "partial_update", "destroy"
    )
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner