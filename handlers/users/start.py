import encodings
from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import decode_payload

from filters import IsPrivate, IsAdmin, MyFilter
from loader import dp
from re import compile


@dp.message_handler(Command('myCommand', prefixes="!"))
async def bot_command_withoutlink(message: types.Message):
    await message.answer(f"!")


@dp.message_handler(CommandStart(deep_link=None), MyFilter())
async def bot_get_start_deeplink(message: types.Message):
    id_message = message.chat.id
    await message.answer(f"Your payload:{id_message}")


@dp.message_handler(CommandStart(deep_link=compile(r"Zm.*")))
async def bot_get_start_deeplink(message: types.Message):
    args = message.get_args()
    payload = decode_payload(args)
    await message.answer(f"Your payload: {payload}")


# Этот хендлер используется для диплинков в личной переписке:
# Когда пользователь переходит по ссылке http://t.me/username_bot?start=123
# Тогда по нажатию на кнопку start - боту приходит команда старт с аргументом 123
# Тогда мы можем отловить этот диплинк с помощью регулярных выражений (функция compile)
# \d\d\d - значит, что мы ловим 3 цифры подряд. (\d) - одна цифра
@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    # С помощью функции get_args забираем аргументы после команды start. (для примера выше - будет "123")
    deep_link_args = message.get_args()

    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде есть диплинк\n'
                         f'Вы передали аргумент {deep_link_args}.\n')


# В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше
@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start(message: types.Message):
    # Для создания диплинк-ссылки - нужно получить юзернейм бота
    bot_user = await dp.bot.get_me()

    # Формируем диплинк-ссылку
    deep_link = f"http://t.me/{bot_user.username}?start=123"
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде нет диплинка.\n'
                         f'Ваша диплинк ссылка - {deep_link}')
