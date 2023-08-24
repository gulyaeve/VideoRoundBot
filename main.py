import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import video_note, start, any_text
from config import settings


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=settings.TOKEN)


async def main():
    # Объект диспетчера
    dp = Dispatcher()

    # Добавляем роутеры из хэндлеров в диспетчер
    dp.include_router(start.router)
    dp.include_router(video_note.router)
    dp.include_router(any_text.router)

    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
