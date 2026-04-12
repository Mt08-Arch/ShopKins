ALLOWED_IPS = ["1.2.3.4", "5.6.7.8"] 
def is_trusted_ip(ip: str) -> bool:
    return ip in ALLOWED_IPS
