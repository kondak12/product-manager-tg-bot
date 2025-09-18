from service import TaskService, TaskRepository


TOKEN = "TOKEN"

TASK_REPOSITORY = TaskRepository("database.db")
TASK_SERVICE = TaskService(TASK_REPOSITORY)