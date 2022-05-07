from datetime import datetime
import pytest

from domain_models import User


@pytest.fixture(scope="module")
def db_fixture():
    from arango import ArangoClient
    from config import (
        ARANGO_HOST,
        ARANGO_PORT,
        ARANGO_TEST_PASSWORD,
        ARANGO_TEST_USERNAME,
    )

    # Initialize the ArangoDB client.
    client = ArangoClient(
        hosts=f"http://{ARANGO_HOST}:{ARANGO_PORT}",
        resolver_max_tries=1,
    )

    # Connect to "_system" database as root user.
    # This returns an API wrapper for "_system" database.
    sys_db = client.db(
        "_system", username=ARANGO_TEST_USERNAME, password=ARANGO_TEST_PASSWORD
    )

    # Create a new database named "test" if it does not exist.
    if not sys_db.has_database("test"):
        sys_db.create_database("test")

    # Connect to "test" database as root user.
    # This returns an API wrapper for "test" database.
    db = client.db("test", username=ARANGO_TEST_USERNAME, password=ARANGO_TEST_PASSWORD)
    try:
        yield db
    # Delete the database. Note that the new users will remain.
    except:
        db.delete_database("test")


@pytest.fixture(scope="function")
def user_collection(db_fixture):
    # Create a new collection named "user" if it does not exist.
    # This returns an API wrapper for "user" collection.
    if db_fixture.has_collection("users"):
        col = db_fixture.collection("users")
    else:
        col = db_fixture.create_collection("users")
    # Add a hash index to the collection.
    col.add_hash_index(fields=["name"], unique=False)
    try:
        yield col
    except:
        col.delete_collection("users")


@pytest.fixture(scope="function")
def event_collection(db_fixture):
    # Create a new collection named "events" if it does not exist.
    # This returns an API wrapper for "events" collection.
    if db_fixture.has_collection("events"):
        col = db_fixture.collection("events")
    else:
        col = db_fixture.create_collection("events")
    col.add_hash_index(fields=["name"], unique=False)

    try:
        yield col
    except:
        col.delete_collection("events")


@pytest.fixture(scope="function")
def arango_user_repository(user_collection,db_fixture):
    from arango_db_user_repository import ArangoUserRepository

    yield ArangoUserRepository(db_fixture)


@pytest.fixture(scope="function")
def arango_event_repository(event_collection,db_fixture):
    from arango_db_event_repository import ArangoEventRepository

    yield ArangoEventRepository(db_fixture)


@pytest.fixture(scope="function")
def saved_user(arango_user_repository):
    user = User(
        name="Test User",
        created_at=datetime.now(),
        phone="+123456789",
        deleted_at=None,
        id=None,
    )
    got = arango_user_repository.add(user)
    assert got.created_at != None
    assert got.name == "Test User"
    assert got.phone == "+123456789"
    yield got
