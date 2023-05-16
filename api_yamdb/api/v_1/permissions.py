from rest_framework import permissions


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):
    message = ('Для проверенных пользователей в статусе '
               'автора, администратора или модератора '
               'иначе только просмотр.')

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (obj.author == request.user
                    or (request.user.is_authenticated
                        and (request.user.is_moderator
                             or request.user.is_admin))
                    )
                )


class IsAdminOrReadOnly(permissions.BasePermission):
    message = ('Для проверенных пользователей в статусе '
               'администратора иначе только просмотр.')

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_admin)


class IsAdmin(permissions.BasePermission):
    message = 'Для проверенных пользователей в статусе администратора.'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
