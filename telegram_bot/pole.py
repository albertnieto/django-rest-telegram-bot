import re
from telegram_bot.static import (
    REGEX_POLE_TYPE,
)

def poleType(text):
    regex_patters = REGEX_POLE_TYPE
    
    for name, _regex in regex_patters.items():
        if re.match(_regex, text):
            return name