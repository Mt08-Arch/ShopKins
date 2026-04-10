from aiogram import Router

payment_router = Router()

@payment_router.post("/webhook/cryptomus")
async def cryptomus_webhook(payload: dict):
    pass
