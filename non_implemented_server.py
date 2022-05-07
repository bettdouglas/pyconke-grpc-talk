from protos.python_out.event_service_pb2_grpc import EventServiceServicer
from protos.python_out.events import CreateEventRequest, CreateEventResponse


class EventService(EventServiceServicer):
    def CreateEvent(self, request : CreateEventRequest, context) -> CreateEventResponse:
        # get data from request
        # save data to database
        return CreateEventResponse()

    def ListEvents(self, request, context):
        return super().ListEvents(request, context)

    def DeleteEvent(self, request, context):
        return super().DeleteEvent(request, context)

    def UpdateEvent(self, request, context):
        return super().UpdateEvent(request, context)

    def GetEvent(self, request, context):
        return super().GetEvent(request, context)
