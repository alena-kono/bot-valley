from telegram.ext import Updater

from apps.telegram_bot.bot.setup import bot, register_handlers


def start_polling() -> None:
    """Run bot in polling mode. In the scope of this project,
    it is used only in DEBUG mode.
    """

    updater = Updater(bot=bot, use_context=True, workers=1)
    dispatcher = updater.dispatcher
    register_handlers(dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    start_polling()
