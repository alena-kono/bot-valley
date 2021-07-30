import json
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView, View

from apps.telegram_bot.bot.webhook import process_telegram_event
from apps.telegram_bot.models import TelegramUser


class WebhookBotView(View):
    """View that processes push updates from telegram bot (webhook)."""

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        request_body = json.loads(request.body)
        process_telegram_event(request_body)
        logging.info(f"Telegram webhook: {request_body}")
        return HttpResponse({"ok": "POST request processed"}, status_code=200)


webhook_bot_view = WebhookBotView.as_view()


class BotUsersView(LoginRequiredMixin, TemplateView):
    """Template view that outputs a list of all telegram users that use the bot.
    Login is required to access this view.
    """

    template_name = "bot_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = TelegramUser.objects.all()
        context["title"] = "Bot users"
        return context


bot_users_view = BotUsersView.as_view()
