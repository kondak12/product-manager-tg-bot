import asyncio, aiogram

from handlers import start
from config import TOKEN


async def main():
    bot = aiogram.Bot(token=TOKEN)
    dp = aiogram.Dispatcher()
    dp.include_routers(
        start.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())