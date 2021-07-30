from telegram import Update
from telegram.ext import CallbackContext

from apps.telegram_bot.bot.messages import MESSAGES
from apps.telegram_bot.models import TelegramUser


def start(update: Update, context: CallbackContext) -> None:
    """Handler that processes /start command. It sends start message and
    saves telegram user to the database if necessary.
    """

    TelegramUser.update_or_create(update)
    text = MESSAGES.get("start")
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
