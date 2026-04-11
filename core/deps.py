from fastapi import Header, HTTPException
from core.security import verify_token


def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, "Invalid token")

    token = authorization.split(" ")[1]

    payload = verify_token(token)

    if not payload:
        raise HTTPException(401, "Invalid token")
    return payload["user_id"]
