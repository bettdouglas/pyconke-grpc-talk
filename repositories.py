from typing import List
from domain_models import User, Event, LatLng

class UserRepository:
    def add(self, user: User) -> User:
        ...
    def get_user(self, id: str) -> User:
        ...

    def delete(self, user: User) -> User:
        ...

    def delete_by_id(self, id: str) -> User:
        ...

    def update(self, user: User) -> User:
        ...

    def all(self) -> List[User]:
        ...


class EventRepository:
    def add(self, event) -> Event:
        ...

    def delete_event(self, event: Event) -> Event:
        ...

    def delete_event_by_id(self, event_id: Event) -> Event:
        ...

    def update_event(self, event: Event) -> Event:
        ...

    def get_event(self, event_id: str) -> Event:
        ...

    def events(self) -> List[Event]:
        ...

    def get_nearest_events(
        self,
        location: LatLng,
        previous_page: int,
        page_size: int,
    ) -> List[Event]:
        ...