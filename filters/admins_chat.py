from aiogram import types
from aiogram.dispatcher.filters import BoundFilter, Filter

from data.config import admins


# Кастомный фильтр на Приватный чат с ботом
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        print("IsAdmin")
        print(message)
        # Возвращаем результат сравнения
        return message.chat.id in admins

class MyFilter(Filter):
    async def check(self, message: types.Message):
        return True