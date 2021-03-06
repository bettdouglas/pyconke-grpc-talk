# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: domain.proto, event_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class User(betterproto.Message):
    id: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)
    phone: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class LatLng(betterproto.Message):
    latitude: float = betterproto.float_field(1)
    longitude: float = betterproto.float_field(2)


@dataclass(eq=False, repr=False)
class Event(betterproto.Message):
    id: str = betterproto.string_field(1)
    title: str = betterproto.string_field(2)
    description: str = betterproto.string_field(3)
    # date time
    date: datetime = betterproto.message_field(4)
    # udration in hours
    duration: int = betterproto.int32_field(5)
    creator: "User" = betterproto.message_field(6)
    location: str = betterproto.string_field(7)
    latlng: "LatLng" = betterproto.message_field(8)


@dataclass(eq=False, repr=False)
class ListEventRequest(betterproto.Message):
    # The parent resource name, for example, "shelves/shelf1"
    location: "LatLng" = betterproto.message_field(1)
    # The maximum number of items to return.
    page_size: int = betterproto.int32_field(2)
    # The next_page_token value returned from a previous List request, if any.
    previous_page: int = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class ListEventResponse(betterproto.Message):
    # The field name should match the noun "Event" in the method name. There will
    # be a maximum number of items returned based on the page_size field in the
    # request.
    events: List["Event"] = betterproto.message_field(1)
    # Token to retrieve the next page of results, or empty if there are no more
    # results in the list.
    next_page_token: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class GetEventRequest(betterproto.Message):
    # The field will contain name of the resource requested.
    id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CreateEventRequest(betterproto.Message):
    # The Event resource to create. The field name should match the Noun in the
    # method name.
    event: "Event" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class UpdateEventRequest(betterproto.Message):
    # The Event resource which replaces the resource on the server.
    event: "Event" = betterproto.message_field(1)
    # The update mask applies to the resource. For the `FieldMask` definition,
    # see https://developers.google.com/protocol-
    # buffers/docs/reference/google.protobuf#fieldmask
    update_mask: "betterproto_lib_google_protobuf.FieldMask" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class DeleteEventRequest(betterproto.Message):
    # The resource name of the Event to be deleted.
    event_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetEventResponse(betterproto.Message):
    # The field name should match the noun in the method name.
    event: "Event" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CreateEventResponse(betterproto.Message):
    # The field name should match the noun in the method name.
    event: "Event" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class UpdateEventResponse(betterproto.Message):
    event: "Event" = betterproto.message_field(1)


class EventServiceStub(betterproto.ServiceStub):
    async def list_events(
        self, *, location: "LatLng" = None, page_size: int = 0, previous_page: int = 0
    ) -> "ListEventResponse":

        request = ListEventRequest()
        if location is not None:
            request.location = location
        request.page_size = page_size
        request.previous_page = previous_page

        return await self._unary_unary(
            "/events.EventService/ListEvents", request, ListEventResponse
        )

    async def get_event(self, *, id: str = "") -> "GetEventResponse":

        request = GetEventRequest()
        request.id = id

        return await self._unary_unary(
            "/events.EventService/GetEvent", request, GetEventResponse
        )

    async def create_event(self, *, event: "Event" = None) -> "CreateEventResponse":

        request = CreateEventRequest()
        if event is not None:
            request.event = event

        return await self._unary_unary(
            "/events.EventService/CreateEvent", request, CreateEventResponse
        )

    async def update_event(
        self,
        *,
        event: "Event" = None,
        update_mask: "betterproto_lib_google_protobuf.FieldMask" = None,
    ) -> "UpdateEventResponse":

        request = UpdateEventRequest()
        if event is not None:
            request.event = event
        if update_mask is not None:
            request.update_mask = update_mask

        return await self._unary_unary(
            "/events.EventService/UpdateEvent", request, UpdateEventResponse
        )

    async def delete_event(
        self, *, event_id: str = ""
    ) -> "betterproto_lib_google_protobuf.Empty":

        request = DeleteEventRequest()
        request.event_id = event_id

        return await self._unary_unary(
            "/events.EventService/DeleteEvent",
            request,
            betterproto_lib_google_protobuf.Empty,
        )


class EventServiceBase(ServiceBase):
    async def list_events(
        self, location: "LatLng", page_size: int, previous_page: int
    ) -> "ListEventResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_event(self, id: str) -> "GetEventResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def create_event(self, event: "Event") -> "CreateEventResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_event(
        self, event: "Event", update_mask: "betterproto_lib_google_protobuf.FieldMask"
    ) -> "UpdateEventResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delete_event(
        self, event_id: str
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_list_events(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "location": request.location,
            "page_size": request.page_size,
            "previous_page": request.previous_page,
        }

        response = await self.list_events(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_get_event(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "id": request.id,
        }

        response = await self.get_event(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_create_event(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "event": request.event,
        }

        response = await self.create_event(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_update_event(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "event": request.event,
            "update_mask": request.update_mask,
        }

        response = await self.update_event(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_delete_event(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "event_id": request.event_id,
        }

        response = await self.delete_event(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/events.EventService/ListEvents": grpclib.const.Handler(
                self.__rpc_list_events,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListEventRequest,
                ListEventResponse,
            ),
            "/events.EventService/GetEvent": grpclib.const.Handler(
                self.__rpc_get_event,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetEventRequest,
                GetEventResponse,
            ),
            "/events.EventService/CreateEvent": grpclib.const.Handler(
                self.__rpc_create_event,
                grpclib.const.Cardinality.UNARY_UNARY,
                CreateEventRequest,
                CreateEventResponse,
            ),
            "/events.EventService/UpdateEvent": grpclib.const.Handler(
                self.__rpc_update_event,
                grpclib.const.Cardinality.UNARY_UNARY,
                UpdateEventRequest,
                UpdateEventResponse,
            ),
            "/events.EventService/DeleteEvent": grpclib.const.Handler(
                self.__rpc_delete_event,
                grpclib.const.Cardinality.UNARY_UNARY,
                DeleteEventRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
        }


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
