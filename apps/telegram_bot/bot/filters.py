import telegram
from telegram.ext.filters import MessageFilter

from apps.telegram_bot.preferences import global_preferences


class CryptoCurrencyFilter(MessageFilter):
    """A custom MessageFilter that filters telegram text messages by
    the condition of entering the list of BUTTONS_CRYPTO_CURRENCIES_FROM.
    """

    def filter(self, message: telegram.Message) -> bool:
        currencies_str = global_preferences.get("buttons__crypto_currencies_from")
        currencies_str.replace(" ", "")
        currencies_list = currencies_str.split(",")
        if message.text in currencies_list:
            return True
        return False
