import hashlib
import json

class CryptomusClient:
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self.api_key = api_key
