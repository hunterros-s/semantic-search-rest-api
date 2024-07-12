import flask
import semantic_search

from semantic_search.core.embedding import embed, embed_single, embed_query
from semantic_search.core.parse_file import parse_file