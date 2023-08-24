from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Отправь мне видео и я сделаю его кружочком)\n\n"
                         "Кстати, я пока работаю в тестовом режиме, присылайте мне обратную связь простым текстом)")
