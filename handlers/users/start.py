from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.texts import text
from filters import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(text.start_message.format(message.from_user.full_name))

