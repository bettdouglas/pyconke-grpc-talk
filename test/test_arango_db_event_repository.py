import datetime
from domain_models import Event, LatLng, User


def test_can_add_event(arango_event_repository,saved_user):
    event = Event(
        title="Mock Event",
        description="Mock description",
        location=LatLng(lat=0,lng=0),
        location_description="Mock location description",
        start_time=datetime.datetime.now() + datetime.timedelta(days=7),
        duration=3600,
        created_at=None,
        creator=saved_user,
        attendees=[],
        deleted_at=None,
        id=None,
    )
    got = arango_event_repository.add(event)
    assert got.id != None
    assert got.creator == saved_user
    assert got.attendees == []
    assert got.deleted_at == None
    assert got.title == "Mock Event"
    assert got.description == "Mock description"
    assert got.location == LatLng(lat=0,lng=0)
    assert got.location_description == "Mock location description"
    assert type(got.start_time) == datetime.datetime
    assert got.duration == 3600
    assert got.created_at != None
        

def can_delete_event(arango_event_repository,saved_user):
    pass

def can_update_event(arango_event_repository,saved_user):
    pass

def can_get_events(arango_event_repository,saved_user):
    pass

def can_get_events_by_user(arango_event_repository,saved_user):
    pass

def can_get_nearby_events(arango_event_repository,saved_user):
    pass

def can_get_events_by_date(arango_event_repository,saved_user):
    pass

def can_get_events_by_date_and_user(arango_event_repository,saved_user):
    pass
