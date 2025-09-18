import aiosqlite

from models import Task


class UserRepository:

    def __init__(self, db_path: str):
        self.__db_path = db_path

    async def init_tables(self) -> None:
        sql_command = """
        CREATE TABLE IF NOT EXISTS `Users` (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `pincode` INTEGER
        );
    """
        async with aiosqlite.connect(self.__db_path) as db:
            await db.execute(sql_command)
            await db.commit()

    async def create_user(self, telegram_id: int, pincode: int):
        sql_command = """
            INSERT INTO `Users` (`username`, `pincode`) VALUES (
                ?, ?
            );
        """
        async with aiosqlite.connect(self.__db_path) as db:
            db.row_factory = aiosqlite.Row

            await db.execute(sql_command, [telegram_id, pincode])
            await db.commit()

    async def get_pincode(self, username: int):
        async with aiosqlite.connect(self.__db_path) as db:
            cursor = await db.execute(
                "SELECT `pincode` FROM `Users` WHERE `username` == ?;",
                [username]
            )
        pincode = await cursor.fetchone()

        return pincode


class TaskRepository:
    def __init__(self, db_path: str):
        self.__db_path = db_path

    async def init_tables(self) -> None:
        sql_command = """
                CREATE TABLE IF NOT EXISTS `Tasks` (
                    `user_id` TEXT NOT NULL,
                    `id` INTEGER AUTOINCREMENT,
                    `name` INTEGER NOT NULL,
                    `description` TEXT,
                    `deadline` DATETIME NOT NULL,
                    `created_at` TEXT DEFAULT CURRENT_TIMESTAMP
                    FOREIGN KEY (`user_id`) REFERENCES `Users`.`id`
                );
            """
        async with aiosqlite.connect(self.__db_path) as db:
            await db.execute(sql_command)
            await db.commit()

    async def add_new_task(self,
                          user_id: int,
                          name: str,
                          description: str,
                          deadline: str
                          ) -> Task:

        sql_command = """
                INSERT INTO `Tasks` (`name`, `description`, `deadline`)
                    WHERE `user_id` == ?
                    VALUES (?, ?, ?);
            """

        async with aiosqlite.connect(self.__db_path) as db:
            db.row_factory = aiosqlite.Row

            await db.execute(sql_command, [user_id, name, description, deadline])
            await db.commit()

            cursor = await db.execute(
                """
                SELECT * FROM `Tasks` 
                    WHERE `user_id` = ? AND `name` == ?;
                """, [user_id, name]
            )
            row_task = await cursor.fetchone()
            return Task(**dict(row_task))

    async def get_task(self, user_id: int, task_name: str) -> Task:
        async with aiosqlite.connect(self.__db_path) as db:
            cursor = await db.execute(
                """
                SELECT * FROM `Tasks` 
                    WHERE `user_id` = ? AND `name` == ?;
                """, [user_id, task_name]
            )
            row_task = await cursor.fetchone()
            return Task(**dict(row_task))

    async def get_task_list(self, user_id: str) -> list[Task]:
        async with aiosqlite.connect(self.__db_path) as db:
            db.row_factory = aiosqlite.Row

            cursor = await db.execute(
                """
                SELECT * FROM `Tasks`"
                    WHERE `user_id` == ?;
                """, [user_id]
            )

            return [
                Task(**dict(row_task))
                for row_task in await cursor.fetchall()
            ]