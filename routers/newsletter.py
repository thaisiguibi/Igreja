from fastapi import APIRouter, Depends
from models.newsletter import NewsletterCreate
from services import newsletter as newsletter_serv
from models.common import ResponseModel
from core.security import get_current_user

router = APIRouter(prefix="/newsletter")


@router.post("/subscribe")
def subscribe(data: NewsletterCreate):
    return newsletter_serv.subscribe(data.email)


@router.get("/")
def list_subscribers(
    current_user: int = Depends(get_current_user)
):
    return newsletter_serv.list_subscribers()
