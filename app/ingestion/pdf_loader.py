from pathlib import Path

from pypdf import PdfReader

from app.ingestion.models import PDFPageContent


class PDFLoader:
    """Load text content from PDF files page by page."""

    def load(self, file_path: Path) -> list[PDFPageContent]:
        if file_path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected a PDF file, got: {file_path.name}")

        reader = PdfReader(str(file_path))
        pages: list[PDFPageContent] = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            pages.append(
                PDFPageContent(
                    filename=file_path.name,
                    page=page_number,
                    text=text.strip(),
                )
            )

        return pages
