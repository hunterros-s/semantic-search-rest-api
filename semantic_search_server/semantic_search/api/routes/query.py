import flask
import semantic_search
import semantic_search.model
import os
from semantic_search.core.index import Index

@semantic_search.app.route('/api/v1/query/', strict_slashes=False)
def get_queryable_documents():
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