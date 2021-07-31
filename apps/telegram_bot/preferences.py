from preferences import preferences as prefs

# from apps.telegram_bot.bot.default_static import MESSAGES

# MESSAGES = {
#     "start": prefs.TelegramBotPreferences.start_message,
#     "crypto_exchange_rate_error": prefs.TelegramBotPreferences.crypto_exchange_rate_error_message,
#     "any_other_content": prefs.TelegramBotPreferences.any_other_content_message,
#     "error": prefs.TelegramBotPreferences.error_message,
# }

# BUTTONS_CRYPTO_CURRENCIES_FROM = prefs.TelegramBotPreferences.crypto_currencies_from


MESSAGES = {"start": prefs.TelegramBotPreferences.crypto_exchange_rate_error_message}


# BUTTONS_CRYPTO_CURRENCIES_FROM = "BTC"

# MESSAGES = {
#     "start": "start msg",
#     "crypto_exchange_rate_error": "rate error msg",
#     "any_other_content": "any error msg",
# }


# def main():
#     print(TelegramBotPreferences.objects.all())
