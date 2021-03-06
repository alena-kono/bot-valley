from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.telegram_bot.views import webhook_bot_view

app_name = "telegram_bot"
urlpatterns = [
    path(
        f"{settings.TELEGRAM_API_TOKEN}",
        view=csrf_exempt(webhook_bot_view),
        name="webhook",
    ),
]
