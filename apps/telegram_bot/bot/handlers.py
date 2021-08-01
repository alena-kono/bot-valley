from telegram import Update
from telegram.ext import CallbackContext

from apps.cryptocurrency.cryptocompare_api import cryptocompare_api
from apps.telegram_bot.bot.default_static import CRYPTO_CURRENCIES_TO
from apps.telegram_bot.bot.keyboards import get_crypto_currencies_keyboard
from apps.telegram_bot.models import TelegramUser
from apps.telegram_bot.preferences import global_preferences


def start(update: Update, context: CallbackContext) -> None:
    """Handler that processes /start command. It sends start message and
    saves telegram user to the database if necessary.
    """

    TelegramUser.update_or_create(update)
    text = global_preferences.get("messages__start")
    keyboard = get_crypto_currencies_keyboard()
    update.message.reply_text(text=text, reply_markup=keyboard)


def crypto_exchange_rate(update: Update, context: CallbackContext) -> None:
    """Handler that processes pressing cryptocurrencies keyboard buttons.
    It sends a reply containing current exchange rate of received cryptocurrency.
    """

    crypto_requested_from_ = update.message.text
    to_ = CRYPTO_CURRENCIES_TO
    exchange_rate = cryptocompare_api.get_exchange_rates(
        from_=crypto_requested_from_, to_=to_
    )
    if exchange_rate:
        rate = exchange_rate.get(to_)
        text = f"`1 {crypto_requested_from_} is {rate} USD`"
    else:
        text = global_preferences.get("messages__crypto_exchange_rate_error")
    update.message.reply_text(text=text, parse_mode="Markdown")


def any_other_content(update: Update, context: CallbackContext) -> None:
    """Handler that processes any other content (text, audio, video and etc.)
    received from the user.
    """

    text = global_preferences.get("messages__any_other_content")
    update.message.reply_text(text=text)


def error(update: Update, context: CallbackContext) -> None:
    """Handler that processes errors that occured at the backend.
    It sends user a message about the error.
    """

    text = global_preferences.get("messages__error")
    update.message.reply_text(text=text)
