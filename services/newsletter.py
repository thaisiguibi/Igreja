from repository import newsletter as newsletter_repository
from fastapi import HTTPException

def subscribe(email):
    try:
        newsletter_repository.create_subscription(email)
        return True

    except Exception as e:
        print(e)
        raise HTTPException(500, "Erro ao cadastrar email")

def list_subscribers():
        return newsletter_repository.get_subscribers()
