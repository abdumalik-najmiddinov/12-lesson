from aiogram import Bot, Router, types, F
from aiogram.filters import Command
from config import GROUP_USERNAME, GROUP_USERNAME3, GROUP_USERNAME2,GROUP_USERNAME4
from filters.users_chat import IsPrivate
from keyboard.inline import subscribe_ikm
from keyboard.default import main_menu

router = Router()
GROUP_LIST = [GROUP_USERNAME, GROUP_USERNAME3, GROUP_USERNAME2,GROUP_USERNAME4]


async def check_subscription(bot: Bot, user_id: int) -> bool:
    for group in GROUP_LIST:
        try:
            member = await bot.get_chat_member(chat_id=group, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except Exception:
            return False
    return True



@router.message(IsPrivate(), Command("start"))
async def bot_start(message: types.Message, bot: Bot):
    await message.answer(f"Salom, {message.from_user.full_name}!")

    user_id = message.from_user.id
    is_subscribed = await check_subscription(bot, user_id)

    if is_subscribed:
        await message.reply("Botdan foydalanishingiz mumkin!", reply_markup=main_menu())
    else:
        await message.reply(
            "Botdan foydalanish uchun avval guruhimizga obuna bo'ling:",
            reply_markup=subscribe_ikm())


@router.callback_query(F.data == "tekshirsh")
async def check_sub(callback : types.CallbackQuery):
    userid = callback.from_user.id
    is_sub = await check_subscription(callback.bot, userid)

    if is_sub:
        await callback.message.answer("✅ Botdan Foydlanshingiz mumkin", reply_markup=main_menu())

    else:
        await callback.message.answer("❌ Siz hali obuna bolmadingiz", reply_markup=subscribe_ikm())

    await callback.answer()