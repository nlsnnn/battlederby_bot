import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import load_config, Config
from handlers.user_handlers import user_router
from handlers.other_handlers import other_router

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                        '[%(asctime)s] - %(name)s - %(message)s')
    logger.info("Starting bot...")

    config: Config = load_config('.env')

    bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(other_router)

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())