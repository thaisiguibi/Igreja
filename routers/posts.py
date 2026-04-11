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
def create_post(post: PostCreate,
                user_id: int = Depends(get_current_user)
                ):
    result =  post_service.create_post(post, user_id)

    return {
            "data": result,
            "message": "Post Criado"
            }

@router.delete("/{post_id}")
def delete_post(post_id: int, user_id: int = Depends(get_current_user)):
    post_service.delete_post(post_id, user_id)

    return {
            "data": True,
            "message": "Post deletado"
            }

@router.patch("/{post_id}")
def update_post(post_id: int, post: PostUpdate, user_id: int = Depends(get_current_user)):
    result = post_service.update_post(post_id, post.title, post.content, user_id)
    return {
            "data": result,
            "message": "Post atualizado"
            }

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
