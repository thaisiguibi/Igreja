from repository import newsletter as newsletter_repository
from fastapi import HTTPException

def subscribe(email):
    try:
        newsletter_repository.create_subscription(email)
        return True

    except:
        raise HTTPException(400, "Email já cadastrado")


def list_subscribers():
        return newsletter_repository.get_subscribers()
