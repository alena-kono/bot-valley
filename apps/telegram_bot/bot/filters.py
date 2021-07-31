import telegram
from telegram.ext.filters import MessageFilter

from apps.telegram_bot.bot.manage_data import CRYPTO_CURRENCIES_FROM


class CryptoCurrencyFilter(MessageFilter):
    """A custom MessageFilter that filters telegram text messages by
    the condition of entering the list of CRYPTO_CURRENCIES.
    """

    def filter(self, message: telegram.Message) -> bool:
        if message.text in CRYPTO_CURRENCIES_FROM:
            return True
        return False
