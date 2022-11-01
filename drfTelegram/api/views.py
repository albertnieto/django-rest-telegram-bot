import json
import os

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from drfTelegram.api.authentication import SessionCsrfExemptAuthentication

TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "error_token")

# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
@api_view(["POST"])
@authentication_classes([SessionCsrfExemptAuthentication])
def webhookView(request):
    if request.method == 'POST':
        # Arrives in bytes, have to decode
        content = json.loads(request.body)
        print(content)
        #usernames = [user.username for user in User.objects.all()]
        return Response(status=status.HTTP_201_CREATED)


def send_message(message, request, chat_id):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    response = request.post(
        f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
    )