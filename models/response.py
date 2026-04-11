from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    data: Any
    message: Optional[str] = None
