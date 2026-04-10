from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    amount: str
    currency: str
    order_id: str
