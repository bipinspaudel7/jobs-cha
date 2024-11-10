from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest

from django_object_actions import takes_instance_or_queryset


class ActiveInactiveMixin:
    @classmethod
    def make_active_inactive(
        cls,
        modeladmin: ModelAdmin,
        request: HttpRequest,
        queryset: QuerySet,
        is_active: bool,
    ):
        queryset.update(is_active=is_active)
        count = queryset.count()
        model_name = queryset.model._meta.verbose_name
        status = "active" if is_active else "inactive"
        modeladmin.message_user(
            request, f"{count} {model_name}s are now set to {status}."
        )

    @takes_instance_or_queryset
    def make_active(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action active
        """
        ActiveInactiveMixin.make_active_inactive(
            self,
            request,
            queryset,
            True,
        )

    @takes_instance_or_queryset
    def make_inactive(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action inactive
        """
        ActiveInactiveMixin.make_active_inactive(
            self,
            request,
            queryset,
            False,
        )

    make_active.short_description = "Make active"
    make_inactive.short_description = "Make inactive"
