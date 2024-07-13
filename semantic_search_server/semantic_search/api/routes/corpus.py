"""
Corpus/Data Related Routes

This module defines the routes related to managing the corpus of documents in the semantic search application.
It includes routes for retrieving the entire corpus, retrieving individual document information, 
and initiating the processing of a specific document.

Routes:
- `/api/v1/corpus/`: Retrieves the entire corpus as a JSON object.
- `/api/v1/corpus/<basename>/`: Retrieves information about a specific document in the corpus.
- `/api/v1/corpus/<basename>/process`: Initiates the processing of a specific document.
"""
import flask
import semantic_search
from semantic_search.core import document_processor

@semantic_search.app.route('/api/v1/corpus/', strict_slashes=False)
def corpus():
    """
    Retrieve the Entire Corpus

    This route returns the entire corpus of documents as a JSON object.

    Returns:
        A JSON representation of the entire corpus.
    """
    return flask.jsonify(**semantic_search.model.CORPUS.to_dict())

@semantic_search.app.route('/api/v1/corpus/<basename>/', strict_slashes=False)
def get_document_information(basename):
    """
    Retrieve Information About a Specific Document

    This route returns information about a specific document in the corpus,
    identified by its basename.

    Args:
        basename (str): The basename of the document to retrieve.

    Returns:
        A JSON representation of the document's information.

    Raises:
        404: If the document is not found in the corpus.
    """
    if basename not in semantic_search.model.CORPUS:
        flask.abort(404)
    return flask.jsonify(**semantic_search.model.CORPUS[basename])

@semantic_search.app.route('/api/v1/corpus/<basename>/process', strict_slashes=False)
def process_document(basename):
    """
    Initiate the Processing of a Specific Document

    This route initiates the processing of a specific document in the corpus,
    identified by its basename. It changes the document's status to "processing"
    and processes the document asynchronously.

    Args:
        basename (str): The basename of the document to process.

    Returns:
        A JSON object containing the status of the processing request.

    Raises:
        404: If the document is not found in the corpus.
    """
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