from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


quest_router = Router()


class Questions(StatesGroup):
    sex = State()
    age = State()
    view_count = State()
    favorite_genre = State()


@quest_router.message(Command("stop"))
@quest_router.message(F.text == "stop")
async def stop_quest(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен")


@quest_router.message(Command('quest'))
async def start_quest(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мужской"),
                types.KeyboardButton(text="Женский")
            ]
        ]
    )
    await state.set_state(Questions.sex)
    await message.answer('Для выхода введите "stop"')
    await message.answer("Ваш пол?")


@quest_router.message(F.text, Questions.sex)
async def answer_sex(message: types.Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Questions.age)
    await message.answer("Отлично! Следующий вопрос. Ваш возраст?")


@quest_router.message(F.text, Questions.age)
async def answer_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Введите числовое значение")
    elif int(age) < 1 or int(age) > 100:
        await message.answer("Возраст должен быть от 1 до 101")
    else:
        await state.update_data(age=int(age))
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Ежедневно"),
                    types.KeyboardButton(text="Часто")
                ],
                [
                    types.KeyboardButton(text="Редко"),
                    types.KeyboardButton(text="Не смотрю")
                ]
            ]
        )
        await state.set_state(Questions.view_count)
        await message.reply("Продолжаем. Как часто вы смотрите аниме?")


@quest_router.message(F.text, Questions.view_count)
async def answer_view_count(message: types.Message, state: FSMContext):
    await state.update_data(view_count=message.text)
    await state.set_state(Questions.favorite_genre)
    await message.answer("Хорошо! Какой жанр аниме вы предпочитаете?")


@quest_router.message(F.text, Questions.favorite_genre)
async def answer_favorite_genre(message: types.Message, state: FSMContext):
    await message.answer("Закончили! Спасибо за прохождение.")
