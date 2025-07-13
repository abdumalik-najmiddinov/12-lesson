from aiogram import types, Router, F

from keyboard.default import main_menu
from .dollar_kurs import kurs

router = Router()


@router.message(F.text == "Kurs dollar")
async def start_bot(message: types.Message):
    await message.answer(text=f"Bugungi dollar kursi {kurs} so'm",
                         reply_markup=main_menu())
