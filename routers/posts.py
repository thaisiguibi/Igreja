from fastapi import APIRouter, Depends
from services import posts as post_service
from models.posts import PostCreate, PostResponse, PostUpdate
from models.common import ResponseModel
from core.security import get_current_user

router = APIRouter(prefix="/posts")

@router.get("/{post_id}")
def get_post(post_id: int):
    return {
            "data":post_service.get_post(post_id),
            "message":"Post found"
            }

@router.post("/")
def create_post(
    data: PostCreate,
    current_user: int = Depends(get_current_user)
):
    return post_service.create_post(data, current_user)

@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    current_user: int = Depends(get_current_user)
):
    return post_service.delete_post(post_id, current_user)

@router.put("/{post_id}")
def update_post(
    post_id: int,
    data: PostUpdate,
    current_user: int = Depends(get_current_user)
):
    return post_service.update_post(
        post_id,
        data.title,
        data.content,
        current_user
    )

@router.get("/")
def list_posts(
        limit: int = 10, 
        offset: int = 0,
        title: str | None = None,
        order: str = "asc"
        ):
    posts, total = post_service.list_posts(limit, offset, title, order)
    return ResponseModel(
            data={
                    "itens":posts,
                    "total":total,
                    "limit":limit,
                    "offset":offset
                },
            message = "Posts listados"
             )
