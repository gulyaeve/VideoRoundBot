from aiogram import Router, F, types

from main import bot
from utils import make_round_video

router = Router()


@router.message(F.video)
async def video_to_note(message: types.Message):
    await message.reply("В течение минуты ты получишь кружочек")
    file = message.video.file_id
    await bot.download(file, destination=f"temp/{file}.mp4", timeout=60)
    round_video = await make_round_video(f"temp/{file}.mp4")
    await message.answer_video_note(types.FSInputFile(round_video), length=512)
