class AdminNotification:
    async def send_payment_alert(self, amount: str, order_id: str):
        print(f"[ALERT] New payment received: {amount} (Order: {order_id})")
