from qdrant_client import QdrantClient
from qdrant_client.http import models


def build_qdrant_client(url: str, api_key: str | None = None) -> QdrantClient:
    """Create a Qdrant client from connection settings."""
    kwargs: dict[str, object] = {"url": url, "check_compatibility": False}
    if api_key:
        kwargs["api_key"] = api_key
    return QdrantClient(**kwargs)


def ensure_collection(
    client: QdrantClient,
    collection_name: str,
    vector_size: int,
) -> bool:
    """Create the collection when it does not exist. Returns True if created."""
    if client.collection_exists(collection_name):
        return False

    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE,
        ),
    )
    return True
