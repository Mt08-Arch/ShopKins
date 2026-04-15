import re
def is_valid_crypto_address(address: str):
    return bool(re.match(r'^[13a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
