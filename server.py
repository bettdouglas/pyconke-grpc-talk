import grpc
from concurrent import futures
from repositories import UserRepository, EventRepository

def db():
    from arango import ArangoClient
    from config import (
        ARANGO_HOST,
        ARANGO_PORT,
        ARANGO_TEST_PASSWORD,
        ARANGO_TEST_USERNAME,
    )

    # Initialize the ArangoDB client.
    client = ArangoClient(
        hosts=f"http://{ARANGO_HOST}:{ARANGO_PORT}",
        resolver_max_tries=1,
    )

    # Connect to "_system" database as root user.
    # This returns an API wrapper for "_system" database.
    sys_db = client.db(
        "_system", username=ARANGO_TEST_USERNAME, password=ARANGO_TEST_PASSWORD
    )

# main method
# if __name__ == "__main__":


def server(
    event_repository: EventRepository,
    user_repository: UserRepository,
):

    interceptors = []

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors,
    )

    # add service to server
    from event_service import EventService
    from protos.python_out.event_service_pb2_grpc import add_EventServiceServicer_to_server

    event_service = EventService(event_repository)
    add_EventServiceServicer_to_server(event_service, server)

    # start server
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

def serve_production():
    from data_repositories import ArangoUserRepository,ArangoEventRepository

    database = db()

    event_repository = ArangoEventRepository(database)
    user_repository = ArangoUserRepository(database)

    server(event_repository, user_repository)

def serve_test():
    # fakes
    from data_repositories import InMemoryUserRepository,InMemEventRepository

    event_repository = InMemEventRepository()
    user_repository = InMemoryUserRepository()

    server(event_repository, user_repository)

