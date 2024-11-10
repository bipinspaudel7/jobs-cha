from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest


class PrimarySecondaryMixin:
    @classmethod
    def make_primary_secondary(
        cls,
        modeladmin: ModelAdmin,
        request: HttpRequest,
        queryset: QuerySet,
        is_primary: bool,
    ):
        queryset.update(is_primary=is_primary)
        count = queryset.count()
        model_name = queryset.model._meta.verbose_name
        status = "primary" if is_primary else "secondary"
        modeladmin.message_user(
            request, f"{count} {model_name}s are now set to {status}."
        )

    def make_primary(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action primary
        """
        PrimarySecondaryMixin.make_primary_secondary(
            self,
            request,
            queryset,
            True,
        )

    def make_secondary(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action secondary
        """
        PrimarySecondaryMixin.make_primary_secondary(
            self,
            request,
            queryset,
            False,
        )

    make_primary.short_description = "Make primary"
    make_secondary.short_description = "Make secondary"
