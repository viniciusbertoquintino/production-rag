from fastapi import FastAPI

from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Production RAG",
    version="0.1.0",
    description="Production-oriented RAG system with retrieval evaluation and observability.",
)

app.include_router(chat_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
