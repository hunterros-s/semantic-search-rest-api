"""Corpus/data related routes"""
import flask
import semantic_search
from semantic_search.core import document_processor

@semantic_search.app.route('/api/v1/corpus/', strict_slashes=False)
def corpus():
    return flask.jsonify(**semantic_search.model.CORPUS.to_dict())

@semantic_search.app.route('/api/v1/corpus/<basename>/', strict_slashes=False)
def get_document_information(basename):
    if basename not in semantic_search.model.CORPUS:
        flask.abort(404)
    return flask.jsonify(**semantic_search.model.CORPUS[basename])

@semantic_search.app.route('/api/v1/corpus/<basename>/process', strict_slashes=False)
def process_document(basename):
    if basename not in semantic_search.model.CORPUS:
        flask.abort(404)
    
    if semantic_search.model.CORPUS[basename]['status'] != "uploaded":
        return {
            "status": "failed",
            "comment": "already processed or processing"
        }
    
    semantic_search.model.CORPUS[basename]['status'] = "processing"
    document_processor.process_document_async(basename)
    return {
        "status": "processing"
    }