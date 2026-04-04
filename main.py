import asyncio
import logging
from aiogram import Bot, Dispatcher

# В будущем вынесем в .env
API_TOKEN = 'YOUR_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    
    print("Бот ShopKins инициализирован...")
    # await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
