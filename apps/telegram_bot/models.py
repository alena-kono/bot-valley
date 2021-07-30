from django.db import models
from telegram import Update

from apps.telegram_bot.utils import extract_user_data, prepare_user_data


class TelegramUser(models.Model):
    """A Telegram user or bot."""

    class Meta:
        verbose_name = "Telegram bot user"
        verbose_name_plural = "Telegram bot users"

    user_id = models.IntegerField(verbose_name="User ID", unique=True)
    username = models.CharField(
        verbose_name="@Username", max_length=32, null=True, blank=True
    )
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(
        verbose_name="Last Name", max_length=255, null=True, blank=True
    )
    language_code = models.CharField(max_length=8, null=True, blank=True)
    is_bot = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        verbose_name="First launch of the bot", auto_now_add=True, editable=False
    )

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f"<{cls_name} (username: @{self.username})>"

    @classmethod
    def update_or_create(cls, update: Update) -> None:
        """Update Telegram User or create a new one if necessary with the prepared
        telegram user data extracted from Update object. Return None.
        """

        user_data = extract_user_data(update)
        prepare_user_data(user_data)
        user, is_created = cls.objects.update_or_create(
            user_id=user_data["id"],
            defaults=user_data,
        )
        if is_created:
            user.save()
        return None
