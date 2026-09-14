from datetime import datetime

from pydantic import BaseModel, Field


class PDFPageContent(BaseModel):
    filename: str
    page: int = Field(ge=1)
    text: str


class DOCXContent(BaseModel):
    filename: str
    text: str
    title: str | None = None
    author: str | None = None
    created_at: datetime | None = None
    modified_at: datetime | None = None
