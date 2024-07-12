"""Semantic serach REST API."""
import flask
from pathlib import Path

import semantic_search

from semantic_search.api.main import services
from semantic_search.api.main import redirect_to_services

import semantic_search.api.routes