import flask
import semantic_search
import threading
from annoy import AnnoyIndex
from semantic_search.core import embed
from semantic_search.utils import chunk

def process_document_async(basename):

    def long_running_task():
        try:
            # make utils function for this
            with open(semantic_search.model.CORPUS[basename]['path'], 'rb') as file:
                text = file.read().decode('latin-1')
            
            windowed_sentences = chunk(text)

            if not windowed_sentences:
                raise ValueError("Input sentences are empty")

            t = AnnoyIndex(semantic_search.config.EMBEDDING_SIZE, 'angular')

            embeddings = embed(windowed_sentences)

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