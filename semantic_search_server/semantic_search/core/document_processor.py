import flask
import semantic_search
import threading
from annoy import AnnoyIndex
from semantic_search.core import embed
from semantic_search.core import parse_file

def process_document_async(basename):

    def long_running_task():
        try:

            chunks = parse_file(semantic_search.model.CORPUS[basename]['path'])

            if not chunks:
                raise ValueError("Input sentences are empty")
            
            # need to make an indexing core, should be annoy index and the idx -> chunk storage
            t = AnnoyIndex(semantic_search.config.EMBEDDING_SIZE, 'angular')

            embeddings = embed(chunks)

            for idx, embedding in enumerate(embeddings):
                t.add_item(idx, embedding)
            
            t.build(100)

            name = f"{semantic_search.model.CORPUS[basename]['contents_hash']}.ann"
            path = semantic_search.config.ANNOY_FOLDER/name
            t.save(str(path))

            semantic_search.model.CORPUS[basename]['status'] = "embedded"
            semantic_search.model.CORPUS[basename]['ANNOY_path'] = str(path)
            semantic_search.model.CORPUS.save_corpus()
        except Exception as e:
            semantic_search.model.CORPUS[basename]['status'] = "uploaded"
            print(f"error while processing: {e}")
    
    thread = threading.Thread(target=long_running_task)
    thread.start()