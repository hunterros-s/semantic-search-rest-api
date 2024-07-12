import flask
import sentence_transformers

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

def embed(chunk_list: list[str]):
    return model.encode([f"search_document: {chunk}" for chunk in chunk_list], convert_to_tensor=True)

def embed_single(chunk: str):
    return model.encode([f"search_document: {chunk}"], convert_to_tensor=True)[0]

def embed_query(chunk: str):
    return model.encode([f"search_query: {chunk}"], convert_to_tensor=True)[0]


