"""
Semantic Search API Routes Initialization

This module initializes and registers all the routes for the semantic search API. It imports specific route handlers
for uploading files, managing the corpus, and querying the semantic search index, thereby making them available
to the main Flask application.
"""
import flask
import semantic_search

from semantic_search.api.routes.upload import upload
from semantic_search.api.routes.corpus import corpus
from semantic_search.api.routes.query import get_queryable_documents