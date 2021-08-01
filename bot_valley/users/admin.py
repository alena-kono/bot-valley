from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from bot_valley.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy


# class BotValleyAdminSite(AdminSite):
#     # Text to put at the end of each page"s <title>.
#     site_title = ugettext_lazy("Bot Valley admin")

#     # Text to put in each page"s <h1> (and above login form).
#     site_header = ugettext_lazy("Bot Valley administration")

#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy("Bot Valley administration")

# admin_site = BotValleyAdminSite()
admin.site.site_header = "Bot Valley administration"
