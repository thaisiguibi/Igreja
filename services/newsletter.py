from repository import newsletter as newsletter_repository
from fastapi import HTTPException

def subscribe(email):

    if not email:
        raise HTTPException(400, "Email obrigatório")

    existing = newsletter_repository.get_subscriber_by_email(email)

    if existing:
        raise HTTPException(400, "Email já cadastrado")

    try:
        newsletter_repository.create_subscription(email)
        return True

    except Exception as e:
        print(e)
        raise HTTPException(500, "Erro interno")

def list_subscribers():
    subscribers = newsletter_repository.get_subscribers()

    return {
        "items": subscribers,
        "total": len(subscribers)
    }
