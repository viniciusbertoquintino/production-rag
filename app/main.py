from fastapi import FastAPI

app = FastAPI(
    title="Production RAG",
    version="0.1.0",
    description="Production-oriented RAG system with retrieval evaluation and observability.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
