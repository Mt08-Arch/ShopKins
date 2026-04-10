import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CRYPTOMUS_MERCHANT_ID: str = os.getenv("MERCHANT_ID", "")
    CRYPTOMUS_API_KEY: str = os.getenv("API_KEY", "")
    WEBHOOK_SECRET: str = os.getenv("WEBHOOK_KEY", "")

settings = Settings()
