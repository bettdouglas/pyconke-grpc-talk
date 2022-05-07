from datetime import datetime
from protos.python_out.event_service_pb2_grpc import EventServiceServicer
from protos.python_out.events import (
    CreateEventRequest,
    CreateEventResponse,
    DeleteEventRequest,
    Event,
    GetEventRequest,
    GetEventResponse,
    LatLng,
    ListEventRequest,
    ListEventResponse,
    User,
)
from betterproto.lib.google.protobuf import Empty

from data_repositories import EventRepository
import domain_models as dm


class EventService(EventServiceServicer):
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def _event_to_proto(self, event: dm.Event):
        return Event(
            id=event.id,
            title=event.title,
            description=event.description,
            date=event.date,
            duration=event.duration,
            location=event.location,
            latlng=LatLng(lat=event.location.lat, lng=event.location.lng),
            creator=User(
                id=event.creator.id,
                name=event.creator.name,
                email="na",
                phone=event.creator.phone,
            ),
        )

    def GetEvent(self, request: GetEventRequest, context) -> GetEventResponse:
        event = self.event_repository.get_event(request.id)
        return GetEventResponse(event=self._event_to_proto(event))

    def CreateEvent(self, request: CreateEventRequest, context) -> CreateEventResponse:
        event = dm.Event(
            created_at=datetime.now(),
            title=request.event.title,
            creator=context.user,
            deleted_at=None,
            description=request.event.description,
            duration=request.event.duration,
            location=dm.LatLng(
                lat=request.event.latlng.latitude, lng=request.event.latlng.longitude
            ),
            location_description=request.event.location,
            start_time=request.event.date,
            attendees=[],
        )
        saved_event = self.event_repository.add(event)
        return CreateEventResponse(event=self._event_to_proto(saved_event))

    def DeleteEvent(self, request: DeleteEventRequest, context):
        deleted = self.event_repository.delete_event_by_id(request.event_id)
        return Empty()

    def UpdateEvent(self, request, context):
        raise NotImplementedError()
        # return super().UpdateEvent(request, context)

    def ListEvents(self, request: ListEventRequest, context):
        # get nearby events
        events = self.event_repository.get_nearest_events(
            location=dm.LatLng(),
            previous_page=request.previous_page,
            page_size=request.page_size,
        )
        return ListEventResponse(
            events=[self._event_to_proto(event) for event in events],
            next_page_token=request.previous_page+len(events),
        )
