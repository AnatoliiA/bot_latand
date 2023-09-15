from aiogram import Dispatcher

from .private_chat import IsPrivate
from .admins_chat import IsAdmin, MyFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(MyFilter)