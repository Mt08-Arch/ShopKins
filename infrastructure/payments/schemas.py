from pydantic import BaseModel, Field

class WebhookData(BaseModel):
    order_id: str
    status: str
    merchant_id: str
