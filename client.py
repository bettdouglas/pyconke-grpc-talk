from datetime import datetime
from protos.python_out.event_service_pb2_grpc import EventServiceStub
from protos.python_out.events import ListEventRequest,LatLng,ListEventResponse,CreateEventRequest,Event,CreateEventResponse
import grpc

# channel
channel = grpc.insecure_channel("localhost:50051")

events_client = EventServiceStub(channel)

request = ListEventRequest(
    location=LatLng(latitude=-1.0, longitude=36.5),
    page_size=100,
    previous_page=0,
)
response = events_client.ListEvents(request)

events = response.events
for event in events:
    print(event.title)
    print(event.description)
    print(event.location)
    print(event.latlng)
    print(event.creator.name)

create_event_request = CreateEventRequest(
    event=Event(
        description="test",
        title="test",
        duration=30,
        date=datetime.now(),
        latlng=LatLng(lat=-1.0, lng=36.5),
        location='USIU'
    )
)

response = events_client.CreateEvent(create_event_request)
print(response.event.id)
