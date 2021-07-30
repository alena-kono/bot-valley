from core.exceptions import BaseProjectException


class InvalidTelegramMessageError(BaseProjectException):
    """To be raised when telegram message is empty or invalid."""

    def __init__(self, *args: object) -> None:
        msg = "Telegram message is empty or invalid."
        super().__init__(msg, *args)
