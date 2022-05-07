from domain_models import User, Event, LatLng
from repositories import EventRepository
from datetime import datetime
from typing import List
from arango.database import StandardDatabase
from arango.collection import StandardCollection


class ArangoEventRepository(EventRepository):
    def __init__(self, database: StandardDatabase) -> None:
        self.database = database
        self.collection = database.collection("events")

    def add(self, event: Event) -> Event:
        doc = self.collection.insert(
            {
                "title": event.title,
                "location": [event.location.lng, event.location.lat],
                "location_description": event.location_description,
                "description": event.description,
                "attendees": event.attendees,
                "creator_id": event.creator.id,
                "start_time": event.start_time.utcnow().timestamp(),
                "duration": event.duration,
                "created_at": event.created_at.utcnow().timestamp(),
                "deleted_at": None,
            }
        )
        event.id = doc["_id"]
        return self.get_event_by_id(event.id)

    def delete_event(self, event: Event) -> Event:
        self.collection.delete(event.id)
        return event

    def update_event(self, event: Event) -> Event:
        self.collection.update(
            {
                "_id": event.id,
                "title": event.title,
                "location": [event.location.lng, event.location.lat],
                "location_description": event.location_description,
                "description": event.description,
                "attendees": event.attendees,
                "start_time": event.start_time,
                "duration": event.duration,
            },
        )
        return event

    def _user_from_doc(self, creator_doc) -> User:
        return User(
            id=creator_doc["_id"],
            name=creator_doc["name"],
            phone=creator_doc["phone"],
            created_at=datetime.fromtimestamp(creator_doc["created_at"]),
            deleted_at=datetime.fromtimestamp(creator_doc["deleted_at"])
            if creator_doc["deleted_at"]
            else None,
        )

    def _event_from_doc(self, doc) -> Event:
        creator_doc = doc["creator"]
        user = self._user_from_doc(creator_doc)
        return Event(
            id=doc["_id"],
            title=doc["title"],
            location=LatLng(doc["location"][0], doc["location"][1]),
            location_description=doc["location_description"],
            description=doc["description"],
            attendees=doc["attendees"],
            creator=user,
            start_time=datetime.fromtimestamp(doc["start_time"]),
            duration=doc["duration"],
            created_at=datetime.fromtimestamp(doc["created_at"]),
            deleted_at=doc["deleted_at"],
        )

    def get_event_by_id(self, id: str) -> Event:
        # doc = self.collection.get(id)
        cursor = self.database.aql.execute(
            f"""
            FOR doc IN {self.collection.name}
                FILTER doc._id == @id
                    FOR u IN users
                        FILTER u._id == doc.creator_id
                        LIMIT 1
                LIMIT 1
            RETURN merge(doc, {{"creator": u}})
            """,
            bind_vars={"id": id},
        )
        # join with user collection
        doc = cursor.next()
        return self._event_from_doc(doc)

    def get_all_events(self) -> List[Event]:
        cursor = self.database.aql.execute(
            f"""
            FOR doc IN {self.collection.name}
                FILTER doc._id == @id
                    FOR u IN users
                        FILTER u._id == doc.creator_id
                        LIMIT 1
            RETURN merge(doc, {{"creator": u}})
            """,
            bind_vars={"id": id},
        )
        return [self._event_from_doc(doc) for doc in cursor.batch()]
