import hashlib
import hmac
import secrets

SECRET_KEY = secrets.token_bytes(16)


def generate_user_hmac(email: str, phone_number: str):
    data = f"{email}{phone_number}"
    hash_obj = hmac.new(SECRET_KEY, data.encode(), hashlib.sha256)
    return hash_obj.hexdigest()
