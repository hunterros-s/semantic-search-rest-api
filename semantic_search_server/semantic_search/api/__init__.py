"""
Semantic Search REST API Initialization

This module initializes the Flask application for the semantic search REST API and sets up necessary routes and configurations.

Purpose:
- To set up the Flask app instance for handling semantic search functionalities.
- To ensure that necessary routes and services are correctly imported and registered.
"""
import flask
from pathlib import Path

import semantic_search

from semantic_search.api.main import services
from semantic_search.api.main import redirect_to_services

import semantic_search.api.routes