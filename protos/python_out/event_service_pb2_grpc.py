# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos.python_out.events  as event__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class EventServiceStub(object):
    """Generated according to https://cloud.google.com/apis/design/standard_methods
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEvents = channel.unary_unary(
                '/events.EventService/ListEvents',
                request_serializer=event__service__pb2.ListEventRequest.SerializeToString,
                response_deserializer=event__service__pb2.ListEventResponse.FromString,
                )
        self.GetEvent = channel.unary_unary(
                '/events.EventService/GetEvent',
                request_serializer=event__service__pb2.GetEventRequest.SerializeToString,
                response_deserializer=event__service__pb2.GetEventResponse.FromString,
                )
        self.CreateEvent = channel.unary_unary(
                '/events.EventService/CreateEvent',
                request_serializer=event__service__pb2.CreateEventRequest.SerializeToString,
                response_deserializer=event__service__pb2.CreateEventResponse.FromString,
                )
        self.UpdateEvent = channel.unary_unary(
                '/events.EventService/UpdateEvent',
                request_serializer=event__service__pb2.UpdateEventRequest.SerializeToString,
                response_deserializer=event__service__pb2.UpdateEventResponse.FromString,
                )
        self.DeleteEvent = channel.unary_unary(
                '/events.EventService/DeleteEvent',
                request_serializer=event__service__pb2.DeleteEventRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class EventServiceServicer(object):
    """Generated according to https://cloud.google.com/apis/design/standard_methods
    """

    def ListEvents(self, request, context):
        """rpc MethodName (Request) returns (Response);

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=event__service__pb2.ListEventRequest.FromString,
                    response_serializer=event__service__pb2.ListEventResponse.SerializeToString,
            ),
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=event__service__pb2.GetEventRequest.FromString,
                    response_serializer=event__service__pb2.GetEventResponse.SerializeToString,
            ),
            'CreateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEvent,
                    request_deserializer=event__service__pb2.CreateEventRequest.FromString,
                    response_serializer=event__service__pb2.CreateEventResponse.SerializeToString,
            ),
            'UpdateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEvent,
                    request_deserializer=event__service__pb2.UpdateEventRequest.FromString,
                    response_serializer=event__service__pb2.UpdateEventResponse.SerializeToString,
            ),
            'DeleteEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEvent,
                    request_deserializer=event__service__pb2.DeleteEventRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'events.EventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventService(object):
    """Generated according to https://cloud.google.com/apis/design/standard_methods
    """

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/ListEvents',
            event__service__pb2.ListEventRequest.SerializeToString,
            event__service__pb2.ListEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/GetEvent',
            event__service__pb2.GetEventRequest.SerializeToString,
            event__service__pb2.GetEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/CreateEvent',
            event__service__pb2.CreateEventRequest.SerializeToString,
            event__service__pb2.CreateEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/UpdateEvent',
            event__service__pb2.UpdateEventRequest.SerializeToString,
            event__service__pb2.UpdateEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/DeleteEvent',
            event__service__pb2.DeleteEventRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
