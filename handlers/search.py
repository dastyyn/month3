from aiogram import Router, types, F
from aiogram.filters import Command


search_router = Router()


@search_router.message(Command("search"))
async def search(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Детектив"),
            types.KeyboardButton(text="Романтика"),
        ],
        [
            types.KeyboardButton(text="Иссекай"),
            types.KeyboardButton(text="Сёнэн")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберите жанр аниме:", reply_markup=keyboard)


@search_router.message(F.text == "Детектив")
async def detective(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Death note", reply_markup=kb)


@search_router.message(F.text == "Романтика")
async def romance(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("My Senpai is annoying", reply_markup=kb)


@search_router.message(F.text == "Иссекай")
async def isekai(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Re:Zero", reply_markup=kb)


@search_router.message(F.text == "Сёнэн")
async def shonen(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("One piece", reply_markup=kb)