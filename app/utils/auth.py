import datetime
from datetime import timedelta, datetime
import jwt


def create_access_token(data: dict, expires_delta: timedelta = None, algorithm: str = 'HS256', secret_key: str = ''):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm)
    return encoded_jwt


def decode_jwt(token: str, secret_key: str = '', algorithm: str = 'HS256'):
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invelid Token"
