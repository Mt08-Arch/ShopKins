from datetime import datetime

class User:
    def __init__(self, tg_id, username=None, balance=0.0):
        self.tg_id = tg_id
        self.username = username
        self.balance = balance
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<User(id={self.tg_id}, user={self.username}, bal={self.balance})>"
