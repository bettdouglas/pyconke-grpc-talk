from datetime import datetime
from arango_db_user_repository import ArangoUserRepository
from domain_models import User

def test_can_add_user(arango_user_repository):
    user = User(
        created_at=datetime.now(),
        name="John Doe",
        phone="+123456789",
        deleted_at=None,
        id=None,
    )
    got = arango_user_repository.add(user)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None


def test_can_update_user(arango_user_repository):
    user = User(
        created_at=datetime.now(),
        name="John Doe",
        phone="+123456789",
        deleted_at=None,
        id=None,
    )
    got = arango_user_repository.add(user)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None

    user.name = "Jane Doe"
    user.phone = "+987654321"
    got = arango_user_repository.update(user)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None

def test_can_get_user(arango_user_repository):
    user = User(
        name="John Doe",
        phone="+123456789",
        deleted_at=None,
        created_at=None,
        id=None,
    )
    got = arango_user_repository.add(user)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None

    got = arango_user_repository.get_user_by_id(got.id)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None

def test_can_delete_by_id(arango_user_repository):
    user = User(
        name="John Doe",
        phone="+123456789",
        deleted_at=None,
        created_at=None,
        id=None,
    )
    got = arango_user_repository.add(user)
    assert got.name == user.name
    assert got.phone == user.phone
    assert got.id != None

    got = arango_user_repository.delete_by_id(got.id)
    assert got.name == '--deleted--'
    assert got.phone == '--deleted--'
    assert got.id != None
    assert got.deleted_at != None