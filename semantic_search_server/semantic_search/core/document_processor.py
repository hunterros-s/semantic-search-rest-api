import flask
import semantic_search
import threading
from semantic_search.core import parse_file
from semantic_search.core.index import Index
import semantic_search.model

def process_document_async(basename):

    def long_running_task():
        try:

            chunks = parse_file(semantic_search.model.CORPUS[basename]['path'])

            if not chunks:
                raise ValueError("Input sentences are empty")
            
            i = Index()
            i.apply_chunks(chunks)
            i.embed()
            ann_path, convert_path = i.save(semantic_search.model.CORPUS[basename]['contents_hash'])

            semantic_search.model.CORPUS[basename]['status'] = "embedded"
            semantic_search.model.CORPUS[basename]['ANNOY_path'] = str(ann_path)
            semantic_search.model.CORPUS[basename]['convert_path'] = str(convert_path)
            semantic_search.model.CORPUS.save_corpus()
        except Exception as e:
            semantic_search.model.CORPUS[basename]['status'] = "uploaded"
            print(f"error while processing: {e}")
    
    thread = threading.Thread(target=long_running_task)
    thread.start()