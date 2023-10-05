from aiogram import executor
from loguru import logger

from handlers.shops_handlers import go_to_store_handler
from handlers.user_handlers import greeting_handler
from system.dispatcher import dp

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


def main() -> None:
    """Запуск бота https://t.me/KozzyVipBot"""
    executor.start_polling(dp, skip_updates=True)
    greeting_handler()
    go_to_store_handler()


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        logger.exception(e)
