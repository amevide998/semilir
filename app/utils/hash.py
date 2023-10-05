import bcrypt
from app.models.password import Password


def hash_password(pwd: str, salt_round: int = 10) -> Password:
    salt = bcrypt.gensalt(salt_round)
    byte_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    hash_pwd = byte_pwd.decode('utf-8')
    return Password(
        hashed_password=hash_pwd,
        salt=salt
    )
