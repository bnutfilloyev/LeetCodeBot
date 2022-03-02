from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushirish"),
            types.BotCommand("help", "Bot haqida ma'lumot olish"),
            types.BotCommand("source", "Bot source kodlari")
        ]
    )
