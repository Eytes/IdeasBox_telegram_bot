import asyncio
import logging

from aiogram import Bot, Dispatcher

from .config import settings


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(settings.token.get_secret_value())
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
