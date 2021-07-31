import typing as t

import telegram

from apps.telegram_bot.bot.manage_data import CRYPTO_CURRENCIES_FROM

Buttons = t.List[str]


def _get_buttons(buttons: Buttons) -> t.List[telegram.KeyboardButton]:
    """Make  nested list of telegram.KeyboardButton objects
    from simple list of strings.
    """

    return [[telegram.KeyboardButton(btn)] for btn in buttons]


def get_crypto_currencies_keyboard() -> telegram.ReplyKeyboardMarkup:
    """Get telegram.ReplyKeyboardMarkup that contains of cryptocurrencies' buttons."""

    buttons = _get_buttons(CRYPTO_CURRENCIES_FROM)
    keyboard = telegram.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
