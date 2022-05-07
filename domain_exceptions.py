from dataclasses import dataclass

# dataclass with exception
@dataclass(frozen=True)
class UserNotFound(Exception):
    user_id: str
    msg: str = "not found"

    def __str__(self) -> str:
        return f"UserNotFound({self.user_id}: {self.msg})"

@dataclass(frozen=True)
class EventNotFound(Exception):
    event_id: str
    msg: str = "not found"

    def __str__(self) -> str:
        return f"EventNotFound({self.event_id},msg: {self.msg})"