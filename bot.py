import asyncio
from funcs import start_handler_func
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await start_handler_func(message)



@dp.message(Command("начатьигру"))
async def cmd_start(message: types.Message):
    await message.answer("начинаю игру...")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
