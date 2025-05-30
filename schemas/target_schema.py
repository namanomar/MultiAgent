from pydantic import BaseModel
from typing import Optional

class TargetSchema(BaseModel):
    product: str
    quantity: int
    urgency: Optional[str]
    status: Optional[str] = "pending"