from rest_framework_mongoengine import serializers
from drfTelegram.api.views import (
    Pole,
    Coin,
    Telegram_User,
    Telegram_Group,
)


class PoleSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Pole
        fields = [
            "type",
            "telegram_user_id",
            "points",
            "tg_date_time",
        ]

class CoinSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Coin
        fields = [
            "name", "date_time",
        ]

class Telegram_UserSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Telegram_User
        fields = [
            "tg_user_id",
            "tg_is_bot", 
            "tg_first_name",
            "tg_username",
            "tg_user_groups_id",
            "poles",
            "coins",
        ]

class Telegram_GroupSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Telegram_Group
        fields = [
            "tg_group_id",
            "tg_group_title",
            "tg_group_type",
        ]