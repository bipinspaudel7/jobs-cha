from django.http import HttpRequest


class SingletonAdminMixin:
    """
    Admin class for models with a single object.
    """

    def has_add_permission(self, request: HttpRequest):
        """
        Disable add permission.
        """
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None):
        """
        Disable delete permission.
        """
        return False
