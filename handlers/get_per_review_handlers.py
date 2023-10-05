from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from keyboards.user_keyboards import create_back_keyboard  # Клавиатуры поста приветствия
from messages.user_messages import get_per_review_post
from system.dispatcher import dp, bot  # Подключение к боту и диспетчеру пользователя


class SomeState(StatesGroup):
    some_state = State()  # Пример состояния, можно добавить дополнительные состояния


@dp.callback_query_handler(lambda c: c.data == "get_per_review")
async def get_per_review(callback_query: types.CallbackQuery, state: FSMContext):
    """Получить 150 руб. за отзыв"""
    back_keyboard = create_back_keyboard()
    await bot.send_message(callback_query.from_user.id, get_per_review_post,
                           reply_markup=back_keyboard,
                           parse_mode=ParseMode.HTML)


def get_per_review_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(get_per_review)
