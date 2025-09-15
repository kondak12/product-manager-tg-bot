from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    id: int
    username: str
    pincode: int

@dataclass(frozen=True)
class Task:
    id: int
    user_id: int
    name: int
    description: str
    deadline: datetime
    priority: str
    complete: bool