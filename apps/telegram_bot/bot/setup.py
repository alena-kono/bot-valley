import logging

from telegram import Bot
from telegram.ext import Dispatcher, Filters, MessageHandler

from apps.telegram_bot.bot.handlers import echo
from config.settings.base import TELEGRAM_API_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def register_handlers(dispatcher: Dispatcher) -> None:
    """Register bot handlers."""

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


def setup() -> tuple[Bot, Dispatcher]:
    """Set up and return bot and dispatcher instances."""

    bot = Bot(token=TELEGRAM_API_TOKEN)
    dispatcher = Dispatcher(bot, update_queue=None, workers=1)
    register_handlers(dispatcher)
    return bot, dispatcher


# Global
bot, dispatcher = setup()
