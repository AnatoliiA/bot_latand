from aiogram import types
from filters import IsPrivate
from loader import dp

from data.config import admins


# В этом хендлере используем фильтры для приватной переписки,
# фильтр на точное совпадение по слову "secret"
# и только для использования пользователей в списке admins
@dp.message_handler(IsPrivate(), text="secret", user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer("Это секретное сообщение, вызванное одним из администраторов "
                         "в личной переписке")
