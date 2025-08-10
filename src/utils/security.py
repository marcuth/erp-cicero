import hashlib

from config import SALT

def hash_password(password: str) -> str:
    return hashlib.sha256((SALT + (password or "")).encode("utf-8")).hexdigest()
