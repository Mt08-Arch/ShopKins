class ShopKinsError(Exception):
    """Base class for exceptions in this module."""
    pass

class DatabaseConnectionError(ShopKinsError):
    """Raised when the database connection fails."""
    pass
