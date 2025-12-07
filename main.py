from asyncio import run
import logging

from aiogram import Bot, Dispatcher

BOT_TOKEN = "8436054391:AAHa3ik2HVDBu0Zi4mGYguQ9xxupAWvt0eA"
ADMIN = 5000611479

dp = Dispatcher()


@dp.startup()
async def on_startup(bot:Bot):
    await bot.send_message(ADMIN, "Bot started")

@dp.shutdown()
async def on_shutdown(bot:Bot):
    await bot.send_message(ADMIN, "Bot stopped")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")