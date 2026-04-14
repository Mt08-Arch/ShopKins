import hashlib
import json

class CryptomusClient:
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self.api_key = api_key

    def generate_signature(self, data: dict) -> str:
        payload = base64.b64encode(json.dumps(data).encode()).decode()
        return hashlib.md5(f"{payload}{self.api_key}".encode()).hexdigest()
    def check_status(self, payment_id: str):
        # Метод для ручного запроса статуса у API
        pass
    def check_status(self, payment_id: str):
        # Метод для ручного запроса статуса у API
        pass
