class AccessMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        # Проверка, не забанен ли юзер в базе
        return await handler(event, data)
