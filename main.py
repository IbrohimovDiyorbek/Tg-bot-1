import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
 
from handlers.start import router

TOKEN = "7620217998:AAEytAOGAw7-KM6AU_LZ7LHQ6lfLhE7K9O8"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s %(asctime)s [line: %(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Good bye!")
