import json
import requests
import os
import logging
import re
from dotenv import load_dotenv, find_dotenv
from telegram_bot.static import (
    REGEX_FILTERS,
)
from telegram_bot.pole import (
    filter_Pole_from_text,
    PoleHandler,
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

class Dispatcher():
    pass

def dispatch(update):
    # Add command case
    def filter(text):
        for _, _regex in REGEX_FILTERS.items():
            if re.match(_regex, text):
                return True

    logger.info(update)
    text = update["message"]["text"]

    # Change to case
    if filter(text):        
        pole_text = filter_Pole_from_text(text)
        pole = PoleHandler(update, pole_text)
        if pole.save_to_mongodb():
            message, chat_id = pole.create_message_string()
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