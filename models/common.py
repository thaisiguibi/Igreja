from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    data: Optional[Any] = None
    message: str = "success"
