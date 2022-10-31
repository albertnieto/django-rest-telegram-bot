import json
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from drfTelegram.api.authentication import SessionCsrfExemptAuthentication

TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "error_token")

# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
@api_view(["POST"])
@authentication_classes([SessionCsrfExemptAuthentication])
def webhookView(request):
    def post(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        print(request.body)
        #usernames = [user.username for user in User.objects.all()]
        return Response("usernames")