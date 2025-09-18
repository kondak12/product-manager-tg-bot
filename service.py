from models import Task
from repositories import TaskRepository


class TaskService:

    def __init__(self, task_repo: TaskRepository):
        self.__task_repo = task_repo

    async def add_task(self, user_id: int, name: str, description: str, deadline: str) -> Task:
        return await self.__task_repo.add_new_task(user_id, name, description, deadline)

    async def get_tasks(self, username: str) -> list[Task]:
        return await self.__task_repo.get_task_list(username)