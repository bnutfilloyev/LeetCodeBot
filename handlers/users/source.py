from aiogram import types

from data.texts import text
from keyboards.inline.source_link import url_keyboard
from loader import dp


@dp.message_handler(commands=['source'])
async def source(msg: types.Message):
    await msg.reply(text.source, reply_markup=url_keyboard)