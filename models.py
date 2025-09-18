from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    id: int
    username: str
    pincode: int

@dataclass(frozen=True)
class Task:
    task_id: int
    name: str
    description: str
    created_at: datetime
    deadline: datetime
    priority: str
    complete: bool