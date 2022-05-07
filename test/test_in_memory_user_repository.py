import pytest
from domain_exceptions import UserNotFound
from domain_models import User
from datetime import time, timedelta
import datetime
import factory
import uuid
import random
from faker import Faker
from data_repositories.in_memory_user_repository import InMemoryUserRepository

class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.LazyAttribute(lambda n: uuid.uuid4().hex)
    name = factory.Faker("name")
    phone = factory.Faker("phone_number")

    created_at = factory.LazyAttribute(lambda n: Faker().date_time())
    deleted_at = None

def can_create_user_repository():
    repo = InMemoryUserRepository()
    assert repo != None

def can_create_user_repository_with_users():
    users = [UserFactory.create() for _ in range(3)]
    repo = InMemoryUserRepository(users)
    assert len(repo.users) == 3

def test_can_add_user():
    user = UserFactory.create()
    repo = InMemoryUserRepository()
    repo.add_user(user)
    assert len(repo.users) == 1


def test_can_get_user():
    user = UserFactory.create()
    repo = InMemoryUserRepository()
    repo.add_user(user)
    got = repo.get_user(user.id)
    assert got.id == user.id

    assert got == user


def test_can_add_users():
    users = [UserFactory.create() for _ in range(3)]
    repo = InMemoryUserRepository()
    for user in users:
        repo.add_user(user)
    assert len(repo.users) == 3


def test_can_update_user():
    user = UserFactory.create()
    repo = InMemoryUserRepository()
    repo.add_user(user)
    user.name = "new name"
    repo.update_user(user)
    got = repo.get_user(user.id)
    assert got.name == "new name"


def test_can_delete_user():
    user = UserFactory.create()
    repo = InMemoryUserRepository()
    repo.add_user(user)
    repo.delete_user(user)
    assert len(repo.users) == 0

    with pytest.raises(UserNotFound):
        repo.get_user(user.id)
