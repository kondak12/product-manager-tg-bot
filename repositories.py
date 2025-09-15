import aiosqlite


class UserRepository:

    def __init__(self, db_path: str):
        self.__db_path = db_path

    async def init_tables(self) -> None:
        sql_command = """
        CREATE TABLE IF NOT EXISTS `Users` (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `username` STRING NOT NULL,
            `pincode` INTEGER NOT NULL
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