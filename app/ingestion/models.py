from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

DocumentSourceType = Literal["pdf", "docx", "csv", "xlsx"]


class Document(BaseModel):
    """Normalized document content extracted from any supported source."""

    filename: str
    source_type: DocumentSourceType
    text: str
    page: int | None = Field(default=None, ge=1)
    row: int | None = Field(default=None, ge=1)
    sheet: str | None = None
    title: str | None = None
    author: str | None = None
    created_at: datetime | None = None
    modified_at: datetime | None = None
