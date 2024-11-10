from django.contrib import admin

from base.admin.abstract.disabled_admin_mixin import DisabledAdminMixin
from base.admin.abstract.enhanced_admin_mixin import EnhancedAdminMixin
from base.models import (
    Bank,
    BankBranch,
    Country,
    District,
    FiscalYear,
    Municipality,
    Province,
    Notification
)


@admin.register(Country)
class CountryAdmin(EnhancedAdminMixin, DisabledAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "is_active",
        "is_primary",
        "name",
    )
    list_filter = (
        "is_active",
        "is_primary",
    )
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Province)
class ProvinceAdmin(EnhancedAdminMixin, DisabledAdminMixin, admin.ModelAdmin):
    list_display = ("id", "is_active", "country", "name")
    list_filter = ("is_active", "country")
    search_fields = ("name",)


@admin.register(District)
class DistrictAdmin(EnhancedAdminMixin, DisabledAdminMixin, admin.ModelAdmin):
    list_display = ("id", "is_active", "province", "name", "name_in_nepali")
    list_filter = ("is_active", "province")
    search_fields = ("name",)


@admin.register(Municipality)
class MunicipalityAdmin(EnhancedAdminMixin, DisabledAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "is_active",
        "district",
        "is_rural",
        "name",
        "ward_limit",
        "name_in_nepali",
    )
    list_filter = ("is_active", "district", "is_rural")
    search_fields = ("name",)


@admin.register(Bank)
class BankAdmin(EnhancedAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "bank_class",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = (
        "bank_class",
        "name",
    )


@admin.register(BankBranch)
class BranchAdmin(EnhancedAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "is_active",
        "bank",
        "name",
        "is_extension",
    )
    list_filter = (
        "is_active",
        "bank",
        "is_extension",
    )
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(FiscalYear)
class FiscalYearAdmin(EnhancedAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "start_date",
        "end_date",
        "status",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Notification)
class NotificationAdmin(EnhancedAdminMixin, admin.ModelAdmin):
    pass
