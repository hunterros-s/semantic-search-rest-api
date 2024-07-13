"""
Semantic Search Core Module Initialization

This module initializes the core functionalities of the semantic search application. It imports essential components 
that handle embedding, file parsing, and other core tasks necessary for the semantic search process.

Purpose:
- To gather and register core functionalities required for the semantic search application.
- To ensure that these functionalities are available for other parts of the application.
"""
import flask
import semantic_search

from semantic_search.core.embedding import embed, embed_single, embed_query
from semantic_search.core.parse_file import parse_file