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


def create_shops_keyboard() -> InlineKeyboardMarkup:
    """Создать клавиатуру для выбора магазина"""
    shops_keyboard = InlineKeyboardMarkup()
    children_backpacks_button = InlineKeyboardButton(text='Детские рюкзаки и сумки 🎒',
                                                     callback_data='children_backpacks_and_bags_store')
    men_bags_purses_button = InlineKeyboardButton(text='Мужские сумки и кошельки 👜', callback_data='men_bags_purses')
    back_button = InlineKeyboardButton(text='Назад ↩️', callback_data='back')
    shops_keyboard.row(children_backpacks_button)
    shops_keyboard.row(men_bags_purses_button)
    shops_keyboard.row(back_button)
    return shops_keyboard


def create_back_keyboard() -> InlineKeyboardMarkup:
    """Создать клавиатуру для выбора магазина"""
    back_keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton(text='Назад ↩️', callback_data='back')
    back_keyboard.row(back_button)
    return back_keyboard


def create_raffle_keyboard() -> InlineKeyboardMarkup:
    """Создать клавиатуру для выбора магазина"""
    raffle_keyboard = InlineKeyboardMarkup()
    what_contest_button = InlineKeyboardButton(text='Что за конкурс?',
                                               callback_data='what_contest')
    participate_button = InlineKeyboardButton(text='Участвовать', callback_data='participate')
    back_button = InlineKeyboardButton(text='Назад ↩️', callback_data='back')
    raffle_keyboard.row(what_contest_button)
    raffle_keyboard.row(participate_button)
    raffle_keyboard.row(back_button)
    return raffle_keyboard


if __name__ == '__main__':
    create_greeting_keyboard()
    create_shops_keyboard()
    create_back_keyboard()
    create_raffle_keyboard()
