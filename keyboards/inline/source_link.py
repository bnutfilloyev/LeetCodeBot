from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import keyboard


url_keyboard = InlineKeyboardMarkup(row_width=1)
url_button = InlineKeyboardButton(text=keyboard.source, url=keyboard.source_url)
url_keyboard.add(url_button)