
from typing import Optional
from pydantic import BaseModel

class Metadata(BaseModel):
    user_id: str
    contract_url: Optional[str]
    contract_name: str
    metadata: dict
    