from fastapi import APIRouter
from services import users as user_service
from models.users import UserCreate, UserResponse
from typing import List
from models.users import LoginRequest
from models.common import ResponseModel
from core.security import create_access_token

router = APIRouter(prefix="/users")

@router.post("/login")
def login(data: LoginRequest):
    return user_service.login(data.name, data.password)

@router.post("/register")
def register(user: UserCreate):
    return user_service.create_user(user.name, user.password)

@router.get("/name/{name}")
def get_user_by_name(name: str):
    user =  user_service.get_user_by_name(name)

    return ResponseModel(
            data=user,
            message="Username found"
            )

@router.get("/")
def list_users(
    limit: int = 10,
    offset: int = 0,
    current_user: int = Depends(get_current_user)
):
    return user_service.list_users(limit, offset)

@router.get("/{user_id}")
def get_user(
    user_id: int,
    current_user: int = Depends(get_current_user)
):
    return user_service.get_user(user_id)

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    current_user: int = Depends(get_current_user)
):
    return user_service.delete_user(user_id, current_user)
