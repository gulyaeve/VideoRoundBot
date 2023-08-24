from aiogram import Router, F, types

from config import settings

router = Router()


@router.message(F.text)
async def send_message_to_bot_admin(message: types.Message):
    await message.forward(settings.ADMIN_ID)
    await message.reply("Отправил ваше сообщение создателю")