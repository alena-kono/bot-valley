from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from apps.telegram_bot.models import TelegramUser

admin.site.unregister([Group, Site])


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    """Representation of a TelegramUser model in the admin interface."""

    list_display = (
        "created_at",
        "user_id",
        "username_with_at_sign",
        "first_name",
        "last_name",
    )
    ordering = ("created_at",)
    fields = (
        "user_id",
        "username",
        "first_name",
        "last_name",
    )
    list_filter = (
        "created_at",
        "language_code",
        "is_bot",
    )
    search_fields = (
        "user_id",
        "username",
        "first_name",
        "last_name",
    )
    list_per_page = 20
    empty_value_display = "-empty-"

    def has_add_permission(self, request, obj=None) -> bool:
        """Remove add permission from the admin interface."""

        return False

    def username_with_at_sign(self, obj: object) -> str:
        """Format TelegramUser's username as '@username'."""

        return f"@{obj.username}"

    username_with_at_sign.short_description = "@username"
