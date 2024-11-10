from django.contrib.admin import ModelAdmin
from django.http import HttpRequest


class DisabledAdminMixin:
    def has_add_permission(self, request: HttpRequest):
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None):
        return False

    def has_change_permission(self, request: HttpRequest, obj=None):
        return False

    def get_actions(self: ModelAdmin, request: HttpRequest):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def get_readonly_fields(self: ModelAdmin, request: HttpRequest, obj=None):
        return [f.name for f in self.model._meta.fields]
