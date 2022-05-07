from uuid import uuid4
from domain_exceptions import EventNotFound
from domain_models import Event
from typing import List
from rtree import index
from repositories import EventRepository,LatLng


class InMemEventRepository(EventRepository):
    def __init__(self):
        super().__init__()
        self.repo = InMemoryRepository()

    def add_event(self, event: Event) -> Event:
        event.id = str(uuid4())
        self.repo.put(event)
        return event

    def delete_event(self, event: Event) -> Event:
        self.repo.remove(event)
        return event

    def update_event(self, event: Event) -> Event:
        self.repo.remove_by_id(event.id)
        self.repo.put(event)
        return event

    def get_event(self, issue_id: str) -> Event:
        got = self.repo.find_by_id(issue_id)
        if got is None:
            raise EventNotFound(issue_id, "not found")
        return got

    def events(self) -> List[Event]:
        return self.repo.find_all()

    def get_nearest_events(
        self, location: LatLng, previous_page: int, page_size: int
    ) -> List[Event]:
        bounds = location.bounds
        events_idx = index.Index()
        for event in self.events():
            add_event_to_index(event, events_idx)

        nearest_n = events_idx.nearest(bounds, page_size, objects="raw")
        return list(nearest_n)


def add_event_to_index(event: Event, idx: index.Index):
    location = event.location
    bounds = location.bounds
    issue_id_hash = hash(event.id)
    idx.insert(issue_id_hash, bounds, event)




import pickle


class BaseRepository:
    def put(self, entity):
        raise NotImplementedError

    def find_by_id(self, entity_id):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    def remove_by_id(self, entity_id):
        raise NotImplementedError

    def remove_all(self):
        raise NotImplementedError

    def drop(self):
        raise NotImplementedError


class InMemoryRepository(BaseRepository):
    KEY_NAME = "id"

    def __init__(self):
        super().__init__()
        self._storage = {}

    def put(self, entity):
        key = self._key(self._get_id(entity))
        self._storage[key] = self._serialize(entity)

    def remove(self, entity):
        key = self._key(self._get_id(entity))
        del self._storage[key]

    def remove_by_id(self, entity_id):
        key = self._key(entity_id)
        self._storage.pop(key, None)

    def remove_all(self):
        self._storage.clear()

    def drop(self):
        self._storage.clear()

    def find_all(self):
        return [self._deserialize(item) for k, item in self._storage.items()]

    def find_by_id(self, entity_id):
        key = self._key(entity_id)
        entity = self._storage.get(key, None)
        if entity:
            return self._deserialize(entity)
        return None

    def _serialize(self, data):
        return pickle.dumps(data)

    def _get_id(self, entity):
        return getattr(entity, self.KEY_NAME)

    def _deserialize(self, data):
        return pickle.loads(data)

    def _key(self, entity_id):
        return entity_id
