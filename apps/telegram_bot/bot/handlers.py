from telegram import Update
from telegram.ext import CallbackContext

from apps.cryptocurrency.cryptocompare_api import CryptoCompareAPI
from apps.telegram_bot.bot.keyboards import get_crypto_currencies_keyboard
from apps.telegram_bot.bot.manage_data import (
    CRYPTO_CURRENCIES_FROM,
    CRYPTO_CURRENCIES_TO,
)
from apps.telegram_bot.bot.static import MESSAGES
from apps.telegram_bot.models import TelegramUser


def start(update: Update, context: CallbackContext) -> None:
    """Handler that processes /start command. It sends start message and
    saves telegram user to the database if necessary.
    """

    TelegramUser.update_or_create(update)
    text = MESSAGES.get("start")
    keyboard = get_crypto_currencies_keyboard()
    update.message.reply_text(text=text, reply_markup=keyboard)


def crypto_exchange_rate(update: Update, context: CallbackContext) -> None:
    """Handler that processes pressing cryptocurrencies keyboard buttons.
    It sends a reply containing current exchange rate of received cryptocurrency.
    """

    crypto_requested = update.message.text
    exchange_rate = CryptoCompareAPI().get_exchange_rates(
        from_=CRYPTO_CURRENCIES_FROM, to_=CRYPTO_CURRENCIES_TO
    )
    if exchange_rate:
        rate = exchange_rate.get(crypto_requested).get("USD")
        text = f"`1 {crypto_requested} is {rate} USD`"
    else:
        text = MESSAGES.get("crypto_exchange_rate_error")
    update.message.reply_text(text=text, parse_mode="Markdown")


def any_other_content(update: Update, context: CallbackContext) -> None:
    """Handler that processes any other content (text, audio, video and etc.)
    received from the user.
    """

    text = MESSAGES.get("any_other_content")
    update.message.reply_text(text=text)
