from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_greeting_keyboard() -> InlineKeyboardMarkup:
    """Создать клавиатуру для приветствия"""
    greeting_keyboard = InlineKeyboardMarkup()
    get_reward_button = InlineKeyboardButton(text='Получить 150₽  за отзыв 💰', callback_data='get_per_review')
    enter_raffle_button = InlineKeyboardButton(text='Участвовать в розыгрыше 5000₽ 🎁', callback_data='raffle')
    visit_store_button = InlineKeyboardButton(text='Перейти в магазин 🛒', callback_data='go_to_store')
    greeting_keyboard.row(get_reward_button)
    greeting_keyboard.row(enter_raffle_button)
    greeting_keyboard.row(visit_store_button)
    return greeting_keyboard


if __name__ == '__main__':
    create_greeting_keyboard()
