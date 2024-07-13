"""REST API for available services."""
import flask
import semantic_search


@semantic_search.app.route('/')
def redirect_to_services():
    """Redirects to services."""
    return flask.redirect('/api/v1/', code=302)


@semantic_search.app.route('/api/v1/')
def services():
    """Returns the available services."""
    context = {
        "upload": "/api/v1/upload/",
        "corpus": "/api/v1/corpus/",
        "query": "/api/v1/query/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)