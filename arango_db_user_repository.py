from repositories import UserRepository
from arango.collection import StandardCollection
from arango.database import StandardDatabase
from domain_models import User
from datetime import datetime


class ArangoUserRepository(UserRepository):
    def __init__(self, database: StandardDatabase) -> None:
        self.users = database.collection("users")
        self.database = database

    def add(self, user: User) -> User:
        doc = self.users.insert(
            {
                "name": user.name,
                "phone": user.phone,
                "created_at": user.created_at.timestamp(),
                "deleted_at": None,
            }
        )
        user.id = doc["_id"]
        return user

    def update(self, user: User) -> User:
        self.users.update(
            {"_id": user.id, "name": user.name, "phone": user.phone},
        )
        return user

    def delete(self, user: User) -> User:
        self.users.update(
            {
                "_id": user.id,
                "_deleted": True,
                "name": "--deleted--",
                "phone": "--deleted--",
                "deleted_at": datetime.now().timestamp(),
            }
        )
        user = self.get_user_by_id(user.id)
        return user

    def get_user_by_id(self, id: str) -> User:
        doc = self.users.get(id)
        return User(
            id=doc["_id"],
            name=doc["name"],
            phone=doc["phone"],
            # datetime from epoch timestamp
            created_at=datetime.fromtimestamp(doc["created_at"]),
            deleted_at=datetime.fromtimestamp(doc["deleted_at"])
            if doc["deleted_at"]
            else None,
        )

    def delete_by_id(self, id: str) -> User:
        self.users.update(
            {
                "_id": id,
                "_deleted": True,
                "name": "--deleted--",
                "deleted_at": datetime.now().timestamp(),
                "phone": "--deleted--",
            }
        )
        doc = self.users.get(id)
        return User(
            id=doc["_id"],
            name=doc["name"],
            phone=doc["phone"],
            created_at=doc["created_at"],
            deleted_at=datetime.fromtimestamp(doc["deleted_at"])
            if doc["deleted_at"] != None
            else None,
        )
