from typing import Any

from pydantic import BaseModel, Field

class GraderDTO(BaseModel):
    documentGraded:bool =Field(description='assign boolean value '
    'if document is relevant to user question')
    def __init__(self,documentGraded = False) -> None:
        self.documentGraded = documentGraded