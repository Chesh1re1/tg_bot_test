import asyncio
import logging
from logic import weather

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config

logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher(storage=MemoryStorage())

async def main():
    dp.include_router(weather.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())