from aiogram import types, Router, F
from aiogram.filters import Command
from filters.groups_chat import IsGroup
import asyncio

router = Router()


@router.message(IsGroup(), F.new_chat_members)
async def start_bot(message: types.Message):
    user_id = message.new_chat_members[0].id
    full_name = message.new_chat_members[0].full_name
    await message.reply(text=f"Xush kelibsiz <a href='tg://user?id={user_id}'>{full_name}</a>",
                        parse_mode="HTML")


@router.message(IsGroup(), F.left_chat_member)
async def start_bot(message: types.Message):
    user_id = message.left_chat_member.id
    full_name = message.left_chat_member.full_name
    if message.left_chat_member.id == message.from_user.id:
        await message.reply(text=f"Guruhni tark etdi <a href='tg://user?id={user_id}'>{full_name}</a>",
                            parse_mode="HTML")
    else:
        await message.reply(text=f"Guruhdan chopildi <a href='tg://user?id={user_id}'>{full_name}</a>",
                            parse_mode="HTML")

