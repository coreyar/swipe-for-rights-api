from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated


class UserVoteRead:
    def has_permission(self, auth: Auth, user_id: str):
        return auth.user['id'] == user_id


class UserVoteWrite:
    def has_permission(self, auth: Auth, user_id: str):
        return auth.user['id'] == user_id
