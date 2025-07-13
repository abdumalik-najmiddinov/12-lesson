from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GROUP_USERNAME, GROUP_USERNAME2, GROUP_USERNAME3, GROUP_USERNAME4


def subscribe_ikm():
    button1 = InlineKeyboardButton(text="Guruhga obuna bo'lish",
                                  url=f"https://t.me/{GROUP_USERNAME.strip('@')}")
    button2 = InlineKeyboardButton(text="Guruhga obuna bo'lish",
                                  url=f"https://t.me/{GROUP_USERNAME2.strip('@')}")
    button3 = InlineKeyboardButton(text="Kanalga obuna bo'lish",
                                  url=f"https://t.me/{GROUP_USERNAME3.strip('@')}")
    button4 = InlineKeyboardButton(text="Kanalga obuna bo'lish",
                                  url=f"https://t.me/{GROUP_USERNAME4.strip('@')}")

    button5 = InlineKeyboardButton(text="Tekshirsh☑️",
                                   callback_data="tekshirsh")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button1],
            [button2],
            [button3],
            [button4],
            [button5]
        ])

    return ikm