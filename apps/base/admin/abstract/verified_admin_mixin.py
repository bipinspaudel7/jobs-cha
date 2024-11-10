from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest


class VerifiedUnverifiedMixin:
    @classmethod
    def make_verified_unverified(
        cls,
        modeladmin: ModelAdmin,
        request: HttpRequest,
        queryset: QuerySet,
        is_verified: bool,
    ):
        queryset.update(is_verified=is_verified)
        count = queryset.count()
        model_name = queryset.model._meta.verbose_name
        status = "verified" if is_verified else "unverified"
        modeladmin.message_user(
            request, f"{count} {model_name}s are now set to {status}."
        )

    def make_verified(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action verified
        """
        VerifiedUnverifiedMixin.make_verified_unverified(
            self,
            request,
            queryset,
            True,
        )

    def make_unverified(self, request: HttpRequest, queryset: QuerySet):
        """
        Make action unverified
        """
        VerifiedUnverifiedMixin.make_verified_unverified(
            self,
            request,
            queryset,
            False,
        )

    make_verified.short_description = "Make verified"
    make_unverified.short_description = "Make unverified"
