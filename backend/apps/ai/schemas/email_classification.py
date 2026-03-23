from pydantic import BaseModel
from typing import Literal


class EmailClassification(BaseModel):
    category: Literal["PRODUTIVO", "IMPRODUTIVO"]
