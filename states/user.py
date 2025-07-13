from aiogram.fsm.state import StatesGroup, State


class GetUserState(StatesGroup):
    phone_number = State()


class WikiState(StatesGroup):
    text = State()


class TarjimonUzState(StatesGroup):
    text = State()
