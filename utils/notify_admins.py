import logging

from aiogram import Dispatcher

from data.config import admins
from aiogram.utils.deep_linking import get_start_link


async def on_startup_notify(dp: Dispatcher):
    link = await get_start_link('foohhjfjfjfjj',encode=True)
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"{link}")
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе с хендлерами и фильтрами!")

        except Exception as err:
            logging.exception(err)
