# from aiogram import types
# from aiogram.dispatcher import FSMContext  # Состояния пользователя
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ParseMode
#
# from keyboards.user_keyboards import create_shops_keyboard  # Клавиатуры поста приветствия
# from messages.user_messages import shops_post
# from system.dispatcher import dp, bot  # Подключение к боту и диспетчеру пользователя
#
#
# class SomeState(StatesGroup):
#     some_state = State()  # Пример состояния, можно добавить дополнительные состояния
#
#
# @dp.callback_query_handler(lambda c: c.data == "go_to_store")
# async def go_to_store(callback_query: types.CallbackQuery, state: FSMContext):
#     """Наши магазины"""
#     shops_keyboard = create_shops_keyboard()
#     await bot.send_message(callback_query.from_user.id, shops_post,
#                            reply_markup=shops_keyboard,
#                            parse_mode=ParseMode.HTML)
#
#
# def go_to_store_handler():
#     """Регистрируем handlers для бота"""
#     dp.register_message_handler(go_to_store)
