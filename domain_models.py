from dataclasses import dataclass,field
from datetime import datetime
from typing import List, Optional

@dataclass()
class CreatedAtAndDeletedAtMixin:
    created_at: datetime
    deleted_at: datetime

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

@dataclass()
class User(CreatedAtAndDeletedAtMixin):
    id: str
    name: str
    phone: str

@dataclass()
class LatLng:
    lat: float
    lng: float

    @property
    def bounds(self):
        return (self.lng, self.lat, self.lng, self.lat)

@dataclass()
class Event(CreatedAtAndDeletedAtMixin):
    id: str
    title: str
    location: LatLng
    location_description: str
    description: str
    attendees: List[User]
    creator: User
    start_time: datetime
    # utc since epoch
    duration: int
