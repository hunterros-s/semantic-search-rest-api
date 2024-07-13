"""
Query Related Routes

This module defines the routes related to querying the semantic search index within the corpus of documents.
It includes routes to retrieve the list of queryable documents and to perform queries on a specific document's index.

Routes:
- `/api/v1/query/`: Retrieves a list of queryable documents from the corpus.
- `/api/v1/query/<hash>`: Performs a search query on the specified document's index and returns the results.
"""
import flask
import semantic_search
import semantic_search.model
import os
from semantic_search.core.index import Index

@semantic_search.app.route('/api/v1/query/', strict_slashes=False)
def get_queryable_documents():
    """
    Retrieve a List of Queryable Documents

    This route returns a list of documents in the corpus that are ready to be queried.
    A document is considered queryable if it has both ANNOY and convert paths and its status is 'embedded'.

    Returns:
        A JSON list of content hashes of the queryable documents.
    """
    documents = []
    for k, v in semantic_search.model.CORPUS.to_dict().items():
        if not "ANNOY_path" in v or not "convert_path" in v or v['status'] != "embedded":
            continue
        documents.append(
            v['contents_hash']
        )
    return flask.jsonify(documents)

@semantic_search.app.route('/api/v1/query/<hash>', strict_slashes=False)
def query(hash):
    """
    Perform a Search Query on a Document's Index

    This route performs a semantic search query on the specified document's index,
    identified by its content hash.

    Args:
        hash (str): The content hash of the document to query.

    Returns:
        A JSON object containing the search results.

    Raises:
        404: If the document with the specified hash is not found.
        400: If the 'query' parameter is missing from the request.
        500: If the ANNOY or convert paths are not available for the specified document.
    """
    contents_hashes = [doc["contents_hash"] for doc in semantic_search.model.CORPUS.to_dict().values()]

    if hash not in contents_hashes:
        flask.abort(404)

    query = flask.request.args.get('query')
    if query is None:
        flask.abort(400)
    
    ann_path = semantic_search.config.ANNOY_FOLDER/f"{hash}.ann"
    convert_path = semantic_search.config.CONVERT_FOLDER/f"{hash}.json"
    if not os.path.exists(ann_path) or not os.path.exists(convert_path):
        flask.abort(500)
    
    index = Index()
    index.load(hash)

    output = index.query(query)

    return flask.jsonify(output)