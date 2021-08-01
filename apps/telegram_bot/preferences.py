"""Provide admin views Preferences objects and a simple interface to preference values.
"""

from dynamic_preferences.forms import global_preference_form_builder
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import LongStringPreference

from apps.telegram_bot.bot.default_static import (
    BUTTONS_CRYPTO_CURRENCIES_FROM,
    MESSAGES,
)

messages = Section("messages", verbose_name="Telegram bot messages")
buttons = Section("buttons", verbose_name="Telegram bot buttons")


@global_preferences_registry.register
class StartMessagePreference(LongStringPreference):
    section = messages
    name = "start"
    verbose_name = "Start"
    help_text = "Message for /start command"
    default = MESSAGES.get("start")
    required = True


@global_preferences_registry.register
class CryptoExchangeRateError(LongStringPreference):
    section = messages
    name = "crypto_exchange_rate_error"
    verbose_name = "Exhange rate error"
    help_text = "Reply message if it's impossible to get crypto exchange rates"
    default = MESSAGES.get("crypto_exchange_rate_error")
    required = True


@global_preferences_registry.register
class AnyOtherContent(LongStringPreference):
    section = messages
    name = "any_other_content"
    verbose_name = "Any other content"
    help_text = "Reply message if user sent any other content"
    default = MESSAGES.get("any_other_content")


@global_preferences_registry.register
class CryptoCurrenciesFrom(LongStringPreference):
    section = buttons
    name = "crypto_currencies_from"
    verbose_name = "Cryptocurrencies buttons"
    help_text = "Buttons (equal to cryptocurrencies). Example: 'BTC,ETH,DOGE'"
    default = BUTTONS_CRYPTO_CURRENCIES_FROM
    required = True


@global_preferences_registry.register
class Error(LongStringPreference):
    section = messages
    name = "error"
    verbose_name = "General Error"
    help_text = "Reply message if something went wrong with the bot"
    default = MESSAGES.get("error")
    required = True


global_preferences = global_preferences_registry.manager()
form_class = global_preference_form_builder()
