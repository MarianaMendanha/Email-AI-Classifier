from pydantic import BaseModel
from typing import Literal


class EmailPipelineResult(BaseModel):
    category: Literal["PRODUTIVO", "IMPRODUTIVO", "ERROR"]
    response: str
