from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from keyboards.user_keyboards import create_raffle_keyboard
from messages.user_messages import raffle_review_post
from system.dispatcher import dp, bot  # Подключение к боту и диспетчеру пользователя


class SomeState(StatesGroup):
    some_state = State()  # Пример состояния, можно добавить дополнительные состояния


@dp.callback_query_handler(lambda c: c.data == "raffle")
async def raffle(callback_query: types.CallbackQuery, state: FSMContext):
    """Получить 150 руб. за отзыв"""
    raffle_keyboard = create_raffle_keyboard()
    await bot.send_message(callback_query.from_user.id, raffle_review_post,
                           reply_markup=raffle_keyboard,
                           parse_mode=ParseMode.HTML)


def raffle_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(raffle)
