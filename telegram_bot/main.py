import json
import requests
import os
import logging
import re
from dotenv import load_dotenv, find_dotenv
from django_rest_telegram.api.models import (
    Pole,
    Coin,
    Telegram_User,
    Telegram_Group,
)
from telegram_bot.static import (
    REGEX_FILTERS,
)
from telegram_bot.pole import (
    poleType,
)

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
    # Telegram sends unix timestamp
    #date = update["message"]["date"]
    #date = datetime.utcfromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z) - ")
    pass

def dispatch(update):
    def filter(text):
        for _, _regex in REGEX_FILTERS.items():
            if re.match(_regex, text):
                return True

    logger.info(update)
    text = update["message"]["text"]

    # Change to case
    if filter(text):        
        pole = poleType(text)
        user = update["message"]["from"]["first_name"]
        message = f"El usuario {user} ha hecho la {pole}"
        chat_id = update["message"]["chat"]["id"]
        send_message(message, chat_id)


def send_message(message, chat_id):
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    response = requests.post(
        f"{TG_URL}{TG_TOKEN}/sendMessage", data=data
    )
    logger.info(response)
    return response