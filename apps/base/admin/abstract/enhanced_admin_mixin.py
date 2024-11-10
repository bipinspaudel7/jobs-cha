from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import HttpRequest

from base.admin.abstract.active_admin_mixin import ActiveInactiveMixin
from base.admin.abstract.primary_admin_mixin import PrimarySecondaryMixin
from base.admin.abstract.verified_admin_mixin import VerifiedUnverifiedMixin
from django_object_actions import DjangoObjectActions


class EnhancedAdminMixin(
    ActiveInactiveMixin,
    PrimarySecondaryMixin,
    VerifiedUnverifiedMixin,
    DjangoObjectActions,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check if the models has the created field
        if hasattr(self.model, "created"):
            self.date_hierarchy = "created"

        if "created" in self.list_display:
            remove_fields = ("created",)
            add_fields = ("_created",)
            self.list_display = tuple(
                field for field in self.list_display if field not in remove_fields
            )
            self.list_display = self.list_display + add_fields

        if "modified" in self.list_display:
            remove_fields = ("modified",)
            add_fields = ("_modified",)
            self.list_display = tuple(
                field for field in self.list_display if field not in remove_fields
            )
            self.list_display = self.list_display + add_fields

        if not getattr(self, "search_fields"):
            _fields = []
            if hasattr(self.model, "name"):
                _fields += ("name",)
            if hasattr(self.model, "title"):
                _fields += ("title",)
            self.search_fields = _fields

    list_per_page = 10

    @admin.display(description="Created", ordering="created")
    def _created(self, obj):
        return naturaltime(obj.created) if hasattr(obj, "created") else "-"

    @admin.display(description="Modified", ordering="modified")
    def _modified(self, obj):
        return naturaltime(obj.modified) if hasattr(obj, "modified") else "-"

    def add_view(
        self,
        request: HttpRequest,
        form_url: str = "",
        extra_context=None,
    ):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        extra_context["show_save_and_continue"] = False
        return super().add_view(request, form_url, extra_context)

    def change_view(
        self,
        request: HttpRequest,
        object_id: int,
        form_url: str = "",
        extra_context=None,
    ):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        extra_context["show_save_and_continue"] = False
        return super().change_view(request, object_id, form_url, extra_context)

    def get_readonly_fields(self, request: HttpRequest, obj=None):
        _readonly_fields = getattr(self, "readonly_fields", [])
        if obj:
            if hasattr(obj, "created"):
                _readonly_fields += ("created",)

            if hasattr(obj, "modified"):
                _readonly_fields += ("modified",)
        return _readonly_fields

    def get_fields(self, request: HttpRequest, obj=None):
        if not obj:
            return super().get_fields(request, obj)
        fields = super().get_fields(request, obj)
        removable_fields = []
        if hasattr(obj, "is_active"):
            removable_fields += ("is_active",)

        if hasattr(obj, "is_primary"):
            removable_fields += ("is_primary",)

        if hasattr(obj, "is_verified"):
            removable_fields += ("is_verified",)
        return tuple(field for field in fields if field not in removable_fields)

    def get_change_actions(self, request: HttpRequest, object_id: int, form_url: str):
        # sourcery skip: assign-if-exp
        actions = super().get_change_actions(request, object_id, form_url)
        add_able_actions = []
        obj = self.get_object(request, object_id)
        if hasattr(obj, "is_active"):
            if obj.is_active:
                add_able_actions += ("make_inactive",)
            else:
                add_able_actions += ("make_active",)

        if hasattr(obj, "is_primary"):
            if obj.is_primary:
                add_able_actions += ("make_secondary",)
            else:
                add_able_actions += ("make_primary",)

        if hasattr(obj, "is_verified"):
            if obj.is_verified:
                add_able_actions += ("make_unverified",)
            else:
                add_able_actions += ("make_verified",)
        return add_able_actions
