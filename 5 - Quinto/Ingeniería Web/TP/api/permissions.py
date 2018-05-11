from rest_framework import permissions

class IsContentOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para solo permitir a los autores editar o eliminar su contenido.
    """

    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura siempre son permitidos para cualquier request, así que siempre se permiten los métodos GET, HEAD y OPTIONS.
        if request.method in permissions.SAFE_METHODS and not obj.elimination_date and (obj.published or obj.response_to):
            return True

        # Los permisos de escritura son concedidos únicamente al usuario autor del contenido.
        return obj.user == request.user

class UserIsNotBanned(permissions.BasePermission):
    """
    Permiso personalizado para no permitir que los usuarios baneados realicen acciones.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated() or (request.user.is_authenticated() and request.user.is_confirmed)

class IsContentOwner(permissions.BasePermission):
    """
    Permiso personalizado para solo permitir que el propio usuario vea sus borradores o contenidos eliminados.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj

class IsNotContentOwner(permissions.BasePermission):
    """
    Permiso personalizado que evalúa que un usuario no sea el autor de un contenido.
    Útil para acciones como 'vote' y 'add_to_favorites'.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user != request.user

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para solo permitir a los autores editar su perfil.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or request.user==obj