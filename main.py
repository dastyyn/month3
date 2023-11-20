import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import my_info_router, picture_router, start_router


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(picture_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
