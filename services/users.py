from repository import users as user_repository
from models.users import UserCreate
from fastapi import HTTPException
from core.security import verify_password, create_access_token, hash_password

def login(name, password):
    user = user_repository.get_user_by_name(name)
    if not user:
        raise HTTPException(404, "User not found")
    if not verify_password(password, user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"user_id": user["id"]})
    return {"access_token": token,
            "token_type": "bearer"
            }

def create_user(name, password):
    existing = user_repository.get_user_by_name(name)
    if existing:
        raise HTTPException(400, "User alredy exists")

    hashed = hash_password(password)
    return user_repository.create_user(name, hashed)

def list_users(limit, offset):
    users, total = user_repository.get_users(limit, offset)

    return {
        "items": users,
        "total": total,
        "limit": limit,
        "offset": offset
    }

def get_user(user_id):
    user = user_repository.get_user(user_id)
    if not user:
        raise HTTPException(
                status_code=404,
                detail="User id not found"
                )
    return user

def get_user_by_name(name):
    user = user_repository.get_user_by_name(name)
    if not user:
        raise HTTPException(
                status_code=404,
                detail="User name not found"
                )
    return user


def delete_user(user_id, current_user):
    user = user_repository.get_user(user_id)

    if not user:
        raise HTTPException(404, "User not found")

    if user_id != current_user:
        raise HTTPException(403, "Not allowed")

    user_repository.deactivate_user(user_id)

    return True
