import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.start import router as start_router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)

    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
