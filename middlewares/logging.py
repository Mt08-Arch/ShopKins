from aiogram import BaseMiddleware
class RequestLoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        # Логируем каждый чих пользователя
        return await handler(event, data)
