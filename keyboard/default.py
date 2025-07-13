from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    button = KeyboardButton(text="Kurs dollar")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True
    )
    return rkm






