"""
Embedding Functions for Semantic Search

This module provides functions for generating embeddings using a pre-trained SentenceTransformer model. 
It includes methods for embedding lists of document chunks, single document chunks, and search queries.
"""
import flask
import sentence_transformers

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

def embed(chunk_list: list[str]):
    """
    Generate Embeddings for a List of Document Chunks

    This function generates embeddings for a list of document chunks using the pre-trained SentenceTransformer model.
    Each chunk is prefixed with "search_document:" to provide context to the model.

    Args:
        chunk_list (list[str]): A list of strings, where each string is a chunk of a document.

    Returns:
        list: A list of embeddings corresponding to the input document chunks.
    """
    return model.encode([f"search_document: {chunk}" for chunk in chunk_list], convert_to_tensor=True)

def embed_single(chunk: str):
    """
    Generate an Embedding for a Single Document Chunk

    This function generates an embedding for a single document chunk using the pre-trained SentenceTransformer model.
    The chunk is prefixed with "search_document:" to provide context to the model.

    Args:
        chunk (str): A string representing a single chunk of a document.

    Returns:
        tensor: The embedding corresponding to the input document chunk.
    """
    return model.encode([f"search_document: {chunk}"], convert_to_tensor=True)[0]

def embed_query(chunk: str):
    """
    Generate an Embedding for a Search Query

    This function generates an embedding for a search query using the pre-trained SentenceTransformer model.
    The query is prefixed with "search_query:" to provide context to the model.

    Args:
        chunk (str): A string representing the search query.

    Returns:
        tensor: The embedding corresponding to the input search query.
    """
    return model.encode([f"search_query: {chunk}"], convert_to_tensor=True)[0]


