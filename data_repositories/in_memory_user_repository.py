from domain_models import User
from repositories import UserRepository
from typing import List
from domain_exceptions import UserNotFound

class InMemoryUserRepository(UserRepository):
    def __init__(self, users: List[User] = None):
        self._users = []
        if users:
            self._users = users

    def add_user(self, user: User) -> User:
        self._users.append(user)
        return self.get_user(user.id)

    def delete_user(self, user: User) -> User:
        found = next((u for u in self._users if u.id == user.id))
        self._users.remove(found)
        return found

    def update_user(self, user: User) -> User:
        found = next((u for u in self._users if u.id == user.id))
        self._users.remove(found)
        self._users.append(user)
        return self.get_user(user.id)

    def get_user(self, user_id: str) -> User:
        found = next((u for u in self._users if u.id == user_id),None)
        if found:
            return found
        raise UserNotFound(f"User with id {user_id} not found")

    @property
    def users(self) -> List[User]:
        return self._users
