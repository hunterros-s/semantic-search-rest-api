"""
REST API for Available Services

This module defines the main entry points for the REST API of the semantic search application. 
It includes routes for redirecting to the main services endpoint and listing the available endpoints.

Routes:
- `/`: Redirects to the `/api/v1/` services root.
- `/api/v1/`: Returns a list of available services and their respective endpoints in JSON format.
"""
import flask
import semantic_search


@semantic_search.app.route('/')
def redirect_to_services():
    """
    Redirect to the Main Services Endpoint

    Redirects the root URL (`/`) to the main services endpoint (`/api/v1/`). 
    This is useful for guiding users or clients to the entry point of the API services.
    
    Returns:
        A 302 HTTP redirect to the `/api/v1/` endpoint.
    """
    return flask.redirect('/api/v1/', code=302)


@semantic_search.app.route('/api/v1/')
def services():
    """
    List Available Services

    Returns a JSON object listing the available services provided by the semantic search API, 
    including upload, corpus, and query functionalities.

    Returns:
        A JSON object containing the available API service endpoints.
        Example:
        {
            "upload": "/api/v1/upload/",
            "corpus": "/api/v1/corpus/",
            "query": "/api/v1/query/",
            "url": "/api/v1/"
        }
    """
    context = {
        "upload": "/api/v1/upload/",
        "corpus": "/api/v1/corpus/",
        "query": "/api/v1/query/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)