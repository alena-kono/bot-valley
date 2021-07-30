import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from django.conf import settings

from apps.telegram_bot.bot.setup import bot
from apps.telegram_bot.bot.start_polling import start_polling

if __name__ == "__main__":

    if settings.DEBUG:
        start_polling()
    else:
        url_parts = [
            "https:/",
            settings.ALLOWED_HOSTS[0],
            "bot",
            settings.TELEGRAM_API_TOKEN,
        ]
        webhook_absolute_url = "/".join([str(_) for _ in url_parts])
        bot.set_webhook(webhook_absolute_url)
