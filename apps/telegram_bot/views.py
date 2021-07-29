import json
import logging

from django.http import HttpRequest, HttpResponse
from django.views import View

from apps.telegram_bot.bot.webhook import process_telegram_event


class WebhookBotView(View):
    """View that processes push updates from telegram bot (webhook)."""

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        request_body = json.loads(request.body)
        process_telegram_event(request_body)
        logging.info(request_body)
        return HttpResponse({"ok": "POST request processed"}, status_code=200)
