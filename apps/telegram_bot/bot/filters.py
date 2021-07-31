import telegram
from telegram.ext.filters import MessageFilter

from apps.telegram_bot.preferences import BUTTONS_CRYPTO_CURRENCIES_FROM


class CryptoCurrencyFilter(MessageFilter):
    """A custom MessageFilter that filters telegram text messages by
    the condition of entering the list of BUTTONS_CRYPTO_CURRENCIES_FROM.
    """

    def filter(self, message: telegram.Message) -> bool:
        if message.text in BUTTONS_CRYPTO_CURRENCIES_FROM:
            return True
        return False
