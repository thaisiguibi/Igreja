from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    title: str
    content: str | None = None

class UserSimple(BaseModel):
    id: int
    name: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str | None
    user: UserSimple

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
