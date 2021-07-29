from telegram import Update
from telegram.ext import CallbackContext


def echo(update: Update, context: CallbackContext) -> None:
    """Handler that echoes the user message."""

    update.message.reply_text(update.message.text)
