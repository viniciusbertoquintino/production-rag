from pydantic import BaseModel, Field


class PDFPageContent(BaseModel):
    filename: str
    page: int = Field(ge=1)
    text: str
