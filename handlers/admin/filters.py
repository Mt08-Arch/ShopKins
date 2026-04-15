from aiogram.filters import Filter
class IsAdmin(Filter):
    async def __call__(self, message):
        return message.from_user.id in [12345678] # Твой ID
