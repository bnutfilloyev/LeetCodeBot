from aiogram import types

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), content_types=[types.ContentType.NEW_CHAT_MEMBERS, types.ContentType.LEFT_CHAT_MEMBER])
async def new_member(message: types.Message):
    await message.delete()