"""Semantic serach rest api server."""
import os
import flask

app = flask.Flask(__name__)

import semantic_search.config
import semantic_search.api
import semantic_search.model
import semantic_search.core
import semantic_search.utils
