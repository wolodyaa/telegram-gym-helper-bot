import logging
import asyncio

from aiogram import Dispatcher, Bot

from app.handlers import router

from config import TOKEN
from app.database import init_db


async def main():
    init_db()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Бот выключен.")