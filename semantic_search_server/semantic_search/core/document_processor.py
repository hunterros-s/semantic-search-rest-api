"""
Document Processor

This module handles the asynchronous processing of documents for the semantic search application. It defines a 
function to process documents in the background, which involves parsing the file, embedding its content, 
and updating the corpus status.
"""
import flask
import semantic_search
import threading
from semantic_search.core import parse_file
from semantic_search.core.index import Index
import semantic_search.model

def process_document_async(basename):
    """
    Process a Document Asynchronously

    This function initiates the asynchronous processing of a document identified by its basename. 
    The process involves parsing the file, embedding its content, and updating its status in the corpus.
    If the processing is successful, it updates the document's status to "embedded" and saves the paths 
    to the ANNOY index and converted file. If an error occurs, it reverts the document's status to "uploaded".

    Args:
        basename (str): The basename of the document to be processed.

    Returns:
        None
    """
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