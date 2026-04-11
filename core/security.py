from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "segredo_super_forte"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

security = HTTPBearer()

#  hash
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        deprecated="auto"
        )

#  senha
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token,
                             SECRET_KEY, 
                             algorithms=[ALGORITHM]
                             )
        return payload

    except JWTError:
        return None


def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(
                token, 
                SECRET_KEY, 
                algorithms=[ALGORITHM])
        return payload["user_id"]

    except JWTError:
        raise HTTPException(401, "Invalid or expired token")
