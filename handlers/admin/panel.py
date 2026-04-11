from aiogram import Router
admin_router = Router()

@admin_router.message()
async def admin_stats(message):
    # Показ статистики продаж и юзеров
    pass
