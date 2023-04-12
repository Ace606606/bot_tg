import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import other_handlers, user_handlers
async def main():
    config = load_config(None)

    bot_token = config.tg_bot.token
    superadmin = config.tg_bot.admin_ids[0]

    bot: Bot = Bot(token=bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    print("Bot offline")
