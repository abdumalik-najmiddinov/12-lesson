from aiogram import Router
from .users import start, kurs
from .groups import ban, member


def setup_message_routers():
    router = Router()
    router.include_router(start.router)
    router.include_router(member.router)
    router.include_router(ban.router)
    router.include_router(kurs.router)

    return router
