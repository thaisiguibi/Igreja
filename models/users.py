from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel): 
    id: int 
    name: str 
    active: bool

class LoginRequest(BaseModel):
    name: str
    password: str
