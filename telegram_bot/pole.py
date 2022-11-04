import re
from datetime import datetime
from mongoengine import *
from telegram_bot.static import (
    REGEX_POLE_TYPE,
    POLE_POINTS,
    POLE_WITH_COIN,
    POLE_WITH_COIN_LIST,
)
from telegram_bot.utils import (
    unix_to_local_timezone,
)
from django_rest_telegram.api.models import (
    Pole,
    Coin,
    TelegramUser,
    TelegramGroup,
)


def filter_Pole_from_text(text):
    regex_patters = REGEX_POLE_TYPE
    
    for name, _regex in regex_patters.items():
        if re.match(_regex, text, re.IGNORECASE):
            return name

class PoleHandler():
    def __init__(self, update, pole_text):
        self.pole_type = pole_text
        self.telegram_user_id = update["message"]["from"]["id"]
        self.is_bot = update["message"]["from"]["is_bot"]
        self.first_name = update["message"]["from"]["first_name"]
        self.tg_date_time = unix_to_local_timezone(update["message"]["date"])
        self.tg_date = self.tg_date_time.date()
        self.chat_id = update["message"]["chat"]["id"]
        self.user = None
        self.pole = None
        self.coin = None
        #self._points = None

    def __str__(self):
        return f"{self.pole_type}: {self.telegram_user_id}, {self.tg_date_time}"

    '''
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value
    '''

    def _user_exists_in_db(self) -> bool:
        telegram_user = TelegramUser(telegram_id=self.telegram_user_id)
        return(telegram_user is not None)

    def _group_exists_in_db(self) -> bool:
        telegram_group = TelegramUser(telegram_id=self.telegram_user_id)
        return(telegram_group is not None)

    def _pole_exists_in_db(self) -> bool:
        count = Pole.objects(
            type=self.pole_type,
            date=self.tg_date,
        ).count()

        return(count>0)

    def _pole_is_valid(self) -> bool:
        pass

    def _is_pole_with_coin(self) -> bool:
        return(self.pole_type in POLE_WITH_COIN_LIST)

    def _get_pole_coins(self) -> bool:
        return(POLE_POINTS[self.pole_type])

    '''
    def _create_user(
        self,
        telegram_id: str,
        is_bot: bool, 
        first_name: str,
        username: str = None,
    ) -> None:
        user = TelegramUser()
        user.telegram_id = telegram_id
        user.is_bot = is_bot
        user.first_name = first_name
        user.username = username
        user.save()

    def _create_pole( 
        self,
        type: str,
        telegram_user_id: str = None, 
        points: int = None,
        date_time: str = None,
    ) -> None:
        pole = Pole()
        pole.type = type
        pole.telegram_user_id = telegram_user_id
        pole.points = points
        pole.date_time = date_time
        pole.save()
    '''

    def _create_pole(self) -> None:
        pole = Pole()
        pole.type = self.pole_type
        pole.telegram_user_id = self.telegram_user_id
        pole.points = self._get_pole_coins()
        pole.date = self.tg_date
        pole.date_time = self.tg_date_time
        pole.save()
        self.pole = pole

    def _create_coin(self) -> None:
        coin = Coin()
        coin.name = POLE_WITH_COIN[self.pole_type]
        coin.telegram_user_id = self.telegram_user_id
        coin.date = self.tg_date
        coin.save()
        self.coin = coin

    def _create_user(self) -> None:
        user = TelegramUser()
        user.telegram_id = self.telegram_user_id
        user.is_bot = self.is_bot
        user.first_name = self.first_name
        #user.username = self.username
        user.save()
        self.user = user

    def _update_user() -> None:
        #telegram_user = TelegramUser(telegram_id=telegram_id)
        pass
        
    def _create_group(self,text) -> None:
        group = TelegramGroup()
        group.telegram_id = ''
        group.title = ''
        group.type = ''
        group.save()

    def _update_group(self,text) -> None:
        pass

    def create_message_string(self) -> str:
        string = "El *usuario* [{}](tg://user?id={}) ha hecho la **{}** 🎉\n".format(self.first_name,self.telegram_user_id, self.pole_type)
        string += "✨ Has ganado **`{} puntos`** ✨".format(self._get_pole_coins())
        if self.coin:
            string += "\nTambién has ganado una **{}** ".format(POLE_WITH_COIN[self.pole_type])
        return string, self.chat_id

    def save_to_mongodb(self):
        if not self._user_exists_in_db():
            self._create_user()
        else:
            self.user = TelegramUser(telegram_id=self.telegram_user_id)

        if not self._pole_exists_in_db():
            if self._is_pole_with_coin():
                self._create_coin()

            self._create_pole()
            #self.user.poles.update_one(push__poles=self.pole)
            #self.user.coins.update_one(push__poles=self.coin)
            return True
        return False


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