"""Corpus/data related routes"""
import flask
import semantic_search
import semantic_search.model

@semantic_search.app.route('/api/v1/corpus/', strict_slashes=False)
def corpus():
    return flask.jsonify(**semantic_search.model.CORPUS.to_dict())


@semantic_search.app.route('/api/v1/corpus/<basename>/', strict_slashes=False)
def get_document_information(basename):
    if not basename in semantic_search.model.CORPUS:
        flask.abort(404)
    
    return flask.jsonify(**semantic_search.model.CORPUS[basename])