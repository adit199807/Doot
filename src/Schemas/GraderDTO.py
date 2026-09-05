from pydantic import BaseModel, Field

class GraderDTO(BaseModel):
    documentGraded:bool =Field(description='assign boolean value '
    'if document is relevant to user question')
