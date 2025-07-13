from aiogram import types, Router, F
from aiogram.filters import Command
from filters.groups_chat import IsGroup
import asyncio

router = Router()
words = ["ahmoq", "jinni", "telba"]


@router.message(IsGroup(), F.text.func(lambda text: any(word in text.lower() for word in words)))
async def start_bot(message: types.Message):
    text = await message.reply("Iltimos dumbul bo'lmang!")
    await message.delete()
    await asyncio.sleep(5)
    await text.delete()
