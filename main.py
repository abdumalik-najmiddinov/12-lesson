import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN, ADMINS
from handler import setup_message_routers

API_TOKEN = BOT_TOKEN
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


async def on_start_up(dispatcher: Dispatcher):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin,
                               text="Bot ishga tushdi")


async def main():
    handler_router = setup_message_routers()
    dp.include_router(handler_router)

    dp.startup.register(on_start_up)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
