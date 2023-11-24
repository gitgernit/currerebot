import asyncio
import aiosqlite
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import config
from funcs import start_handler_func

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message, db):
    await start_handler_func(message, db)


async def main():
    db = await aiosqlite.connect("users.db")
    await db.execute("CREATE TABLE IF NOT EXISTS users_table ("
                     "id INT PRIMARY KEY, "
                     "type TEXT"
                     ")")
    await db.commit()

    try:
        await dp.start_polling(bot, db=db)

    finally:
        await db.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except:
        pass

    finally:
        print('вiключяюсь')
