import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from apps.telegram_bot.bot.start_polling import start_polling

if __name__ == "__main__":
    start_polling()
