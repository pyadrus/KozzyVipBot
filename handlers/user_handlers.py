import datetime  # Дата
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.user_keyboards import create_greeting_keyboard  # Клавиатуры поста приветствия
from messages.user_messages import greeting_post
from system.dispatcher import dp  # Подключение к боту и диспетчеру пользователя


class SomeState(StatesGroup):
    some_state = State()  # Пример состояния, можно добавить дополнительные состояния


@dp.message_handler(commands=['start'])
async def greeting(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия"""
    await state.finish()
    await state.reset_state()
    # Получаем текущую дату и время
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Записываем данные пользователя в базу данных
    # Инициализация базы данных SQLite
    conn = sqlite3.connect('setting/user_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_run (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, 
                                                        first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
    cursor.execute('''INSERT INTO users_run (user_id, first_name, last_name, username, date) VALUES (?, ?, ?, ?, ?)''',
                   (
                       message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                       message.from_user.username,
                       current_date))
    conn.commit()
    print(f'Запустили бота: {message.from_user.id, message.from_user.username, current_date}')
    greeting_keyboard = create_greeting_keyboard()
    # Клавиатура для Калькулятора цен или Контактов
    await message.reply(greeting_post, reply_markup=greeting_keyboard, disable_web_page_preview=True,
                        parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == "back")
async def back(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработчик команды back, он же пост приветствия"""
    await state.finish()
    await state.reset_state()
    # Получаем текущую дату и время
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Запустили бота: {callback_query.from_user.id, callback_query.from_user.username, current_date}')
    greeting_keyboard = create_greeting_keyboard()
    # Отправляем сообщение с клавиатурой в ответ на CallbackQuery
    await callback_query.message.edit_text(
        text=greeting_post,
        reply_markup=greeting_keyboard,
        disable_web_page_preview=True,
        parse_mode=types.ParseMode.HTML
    )



def greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(greeting)  # Обработчик команды /start, он же пост приветствия
    dp.register_message_handler(back)
