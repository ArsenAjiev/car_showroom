from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        return bool(request.user.role == 'CUSTOMER' or request.user.is_superuser)


class IsDealer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        return bool(request.user.role == 'DEALER' or request.user.is_superuser)


class IsShowroom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        return bool(request.user.role == 'SHOWROOM' or request.user.is_superuser)
