import typing as t

import telegram

from apps.telegram_bot.bot.setup import bot, dispatcher

Json = t.Dict[str, t.Any]


def process_telegram_event(update_json: Json) -> None:
    """Process telegram update event by decoding Update
    object and passing it to the dispatcher. Called on webhook.
    """

    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)
