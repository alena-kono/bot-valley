from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.telegram_bot.views import bot_users_view, webhook_bot_view
from config.settings.base import TELEGRAM_API_TOKEN

app_name = "telegram_bot"
urlpatterns = [
    path(f"{TELEGRAM_API_TOKEN}", view=csrf_exempt(webhook_bot_view), name="webhook"),
    path("users/", view=bot_users_view, name="bot users"),
]
