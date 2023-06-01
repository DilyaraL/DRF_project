from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Удалять может только админ, читать могут все"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # если запрос безопасный (GET, HEAD, OPTIONS), те только запросы для чтения
            return True
        # иначе проверим, что пользователь Админ
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если юзер из БД равен Юзеру, что пришел с запросом, то даем доступ
        return obj.user == request.user
