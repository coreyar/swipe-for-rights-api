from rest_framework.serializers import SerializerMethodField

from helpers.serializers import BaseSerializer
from .models import Account


class AccountSerializer(BaseSerializer):
    token: str = SerializerMethodField()

    class Meta:
        model = Account
        fields = ('id', 'token', 'username', 'email', 'first_name', 'last_name',)

    def get_token(self, obj: Account) -> str:
        auth_key: str = obj.auth_token.key
        return auth_key
