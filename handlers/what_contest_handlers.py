from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from keyboards.user_keyboards import create_what_contest_keyboard
from messages.user_messages import what_contest_post
from system.dispatcher import dp, bot  # Подключение к боту и диспетчеру пользователя


class SomeState(StatesGroup):
    some_state = State()  # Пример состояния, можно добавить дополнительные состояния


@dp.callback_query_handler(lambda c: c.data == "what_contest")
async def what_contest(callback_query: types.CallbackQuery, state: FSMContext):
    """Получить 150 руб. за отзыв"""
    what_contest_keyboard = create_what_contest_keyboard()
    await bot.send_message(callback_query.from_user.id, what_contest_post,
                           reply_markup=what_contest_keyboard,
                           parse_mode=ParseMode.HTML)


def what_contest_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(what_contest)