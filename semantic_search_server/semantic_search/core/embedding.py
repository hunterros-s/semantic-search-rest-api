import flask
import sentence_transformers

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

def embed(chunk_list: list[str]):
    return model.encode(chunk_list)

def embed_single(chunk: str):
    return model.encode([chunk])[0]
