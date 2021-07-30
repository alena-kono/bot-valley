import typing as t

from telegram import Update
from telegram.utils.types import JSONDict

from apps.telegram_bot.bot.exceptions import InvalidTelegramMessageError

PreparedTelegramUserData = t.Dict[str, t.Union[int, str, bool]]


def extract_user_data(update: Update) -> JSONDict:
    """Extract telegram user data from telegram Update object."""

    if update.message:
        user_data = update.message.from_user.to_dict()
        return user_data
    raise InvalidTelegramMessageError


def prepare_user_data(user_data: JSONDict) -> PreparedTelegramUserData:
    """Convert is_bot value to bool and update extracted telegram user data in place."""

    is_bot = user_data.get("is_bot")
    if is_bot:
        user_data.update({"is_bot": bool(str(is_bot))})
    return user_data
