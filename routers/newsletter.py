from fastapi import APIRouter
from models.newsletter import NewsletterCreate
from services import newsletter as newsletter_service
from models.common import ResponseModel

router = APIRouter(prefix="/newsletter")

@router.post("/subscribe")

def subscribe(data: NewsletterCreate):
    newsletter_service.subscribe(data.email)

    return ResponseModel(
            data=True,
            message="Inscrição realizada com sucesso"
            )


@router.get("/")
def list_subscribers():
    result = newsletter_service.list_subscribers()

    return {
            "data": result,
            "message": "Emails listados"
            }
