import typing as t

import telegram

from apps.telegram_bot.bot.preferences import BUTTONS_CRYPTO_CURRENCIES_FROM


def _get_buttons(buttons: str) -> t.List[telegram.KeyboardButton]:
    """Make  nested list of telegram.KeyboardButton objects
    from string of the following format: 'KEY1,KEY2,KEY3' or 'KEY1, KEY2, KEY3'.
    """
    buttons_without_spaces = buttons.replace(" ", "")
    buttons_list = buttons_without_spaces.split(",")
    return [[telegram.KeyboardButton(btn)] for btn in buttons_list]


def get_crypto_currencies_keyboard() -> telegram.ReplyKeyboardMarkup:
    """Get telegram.ReplyKeyboardMarkup that contains of cryptocurrencies' buttons."""

    buttons = _get_buttons(BUTTONS_CRYPTO_CURRENCIES_FROM)
    keyboard = telegram.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
