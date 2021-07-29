import telegram
from telegram.utils.types import JSONDict

from apps.telegram_bot.bot.setup import bot, dispatcher


def process_telegram_event(update_json: JSONDict) -> None:
    """Process telegram update event by decoding Update
    object and passing it to the dispatcher. Called on webhook.
    """

    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)
