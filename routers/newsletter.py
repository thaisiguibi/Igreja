from fastapi import APIRouter
from models.newsletter import NewsletterCreate
from services import newsletter as newsletter_service
from models.common import ResponseModel

router = APIRouter(prefix="/newsletter")

@router.post("/")

@router.post("/subscribe")
def subscribe(data: NewsletterCreate):
    return newsletter_service.subscribe(data.email)

@router.get("/")
def list_subscribers(
    current_user: int = Depends(get_current_user)
):
    return newsletter_service.list_subscribers()
