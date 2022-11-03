import json
import os
import logging
from dotenv import load_dotenv, find_dotenv
from typing import Any

load_dotenv(find_dotenv())
logger = logging.getLogger(__name__)

# Telegram Variables
TG_URL = "https://api.telegram.org/bot"
TG_TOKEN = os.getenv("TG_TOKEN")

# Host Variables
HOST_URL = os.getenv("HOST_URL")
WH_ROUTE = os.getenv("WH_ROUTE")

# Webhook URL
WH_URL = f"{TG_URL}{TG_TOKEN}/setWebhook?url={HOST_URL}/{WH_ROUTE}"


class CustomUpdateMF():
    def __init__(
        self,
        user_id,
        user_is_bot=None,
        user_first_name=None,
        username=None,
        chat_id=None,
        chat_title=None,
        chat_type=None,
        date=None,
        text=None,
        entity_type=None,
    ):
        self.user_id = user_id
        self.user_is_bot = user_is_bot
        self.user_first_name = user_first_name
        self.username = username
        self.chat_id = chat_id
        self.chat_title = chat_title
        self.chat_type = chat_type
        self.date = date
        self.text = text
        self.entity_type = entity_type

class Dispatcher():
    pass

def send_message(message, request, chat_id):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    response = request.post(
        f"{TG_URL}/{TG_TOKEN}/sendMessage", data=data
    )
    logger.log(response)
    return response