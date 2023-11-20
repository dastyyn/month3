from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}")
