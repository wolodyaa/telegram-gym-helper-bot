import asyncio, logging

from aiogram import Bot, Dispatcher

from assets.config import TOKEN
from app.handlers import router
from app.database import init_db


async def main():
    init_db()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")