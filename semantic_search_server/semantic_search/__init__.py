"""
Semantic Search REST API Server Initialization

This module sets up the Flask application for the semantic search REST API server. It initializes the main app instance
and imports necessary configurations, models, core functionalities, API routes, and utilities.
"""
import os
import flask

app = flask.Flask(__name__)

import semantic_search.config
import semantic_search.api
import semantic_search.model
import semantic_search.core
import semantic_search.utils
import semantic_search.parsers