from fastapi import APIRouter
from services import users as user_service
from models.users import UserCreate, UserResponse
from typing import List
from models.users import LoginRequest
from models.common import ResponseModel

router = APIRouter(prefix="/users")

@router.get("/")
def list_users(limit: int = 10, offset: int = 0):
    users, total = user_service.list_users(limit, offset)
    return ResponseModel(
            data = {
                "items": users,
                "total": total,
                "limit": limit,
                "offset": offset
                },
            messages="Users listed"
            )

@router.get("/{user_id}")
def get_user(user_id: int):
    user =  user_service.get_user(user_id)

    return ResponseModel(
            data=user,
            message="User found"
            )

@router.get("/name/{name}")
def get_user_by_name(name: str):
    user =  user_service.get_user_by_name(name)

    return ResponseModel(
            data=user,
            message="Username found"
            )

@router.get("/")
def list_users(limit: int = 10, offset: int = 0):
    user =  user_service.list_users(limit, offset)

    return ResponseModel(
            data=user,
            message="List users"
            )

@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = user_service.delete_user(user_id)

    return ResponseModel(
            data=user,
            message="User deleted"
            )

@router.post("/login")
def login(data: LoginRequest):
    user = user_service.login(data.name, data.password)

    return ResponseModel(
            data=user,
            message="User logon"
            )

@router.post("/register")
def register(user: UserCreate):
    user = user_service.create_user(user.name, user.password)

    return ResponseModel(
            data=user,
            message="User registered"
            )
