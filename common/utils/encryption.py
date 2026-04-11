import hashlib
def hash_admin_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()
