from aiogram import BaseMiddleware
class ThrottlingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        # Логика защиты от флуда
        return await handler(event, data)
