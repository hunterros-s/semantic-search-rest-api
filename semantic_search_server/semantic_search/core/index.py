"""
Index Management for Semantic Search

This module provides the `Index` class for managing the indexing, embedding, querying, saving, and loading of document 
chunks using the Annoy library. It includes methods to apply chunks, generate embeddings, perform queries, and 
manage the index files.
"""
import semantic_search
from annoy import AnnoyIndex
import semantic_search.config
from semantic_search.core import embed, embed_query
import json 

class Index:
    def __init__(self) -> None:
        """
        Initialize the Index

        This constructor initializes an Annoy index with the specified embedding size and 
        sets up a dictionary to map index positions to document chunks.
        """
        self.annoy = AnnoyIndex(semantic_search.config.EMBEDDING_SIZE, 'angular')
        self.index_to_word = {}
    
    def apply_chunks(self, chunks: list[str]) -> None:
        """
        Apply Document Chunks to the Index

        This method associates each chunk in the given list with an index position.

        Args:
            chunks (list[str]): A list of document chunks to be indexed.
        """
        for idx, chunk in enumerate(chunks):
            self.index_to_word[idx] = chunk
    
    def embed(self) -> None:
        """
        Generate Embeddings for the Indexed Chunks

        This method generates embeddings for all the document chunks in `index_to_word` and adds them to the Annoy index.
        """
        embeddings = embed(list(self.index_to_word.values()))

        for idx, embedding in enumerate(embeddings):
            self.annoy.add_item(idx, embedding)
        
        self.annoy.build(100)
    
    def query(self, text):
        """
        Perform a Query on the Index

        This method performs a semantic search query on the Annoy index and returns the nearest neighbors 
        and their distances.

        Args:
            text (str): The search query text.

        Returns:
            list: A list of tuples, where each tuple contains a document chunk and its corresponding distance score.
        """
        query_embedding = embed_query(text)

        result_indicies = self.annoy.get_nns_by_vector(query_embedding, 100, include_distances=True)

        result_idxs, scores = (result_indicies[0], result_indicies[1])

        results = [self.index_to_word[i] for i in result_idxs]

        output = list(zip(results, scores))

        return output

    
    def save(self, name: str) -> tuple[str, str]:
        """
        Save the Annoy Index and Mapping to Disk

        This method saves the Annoy index and the dictionary mapping index positions to document chunks to disk.

        Args:
            name (str): The name used to generate the filenames for saving the index and dictionary.

        Returns:
            tuple[str, str]: Paths to the saved Annoy index file and the JSON file containing the index-to-word mapping.
        """
        ann_path = semantic_search.config.ANNOY_FOLDER/f"{name}.ann"
        self.annoy.save(str(ann_path))

        convert_path = semantic_search.config.CONVERT_FOLDER/f"{name}.json"
        with open(convert_path, 'w') as outfile:
            json.dump(self.index_to_word, outfile)
        
        return (ann_path, convert_path)  

    def load(self, name: str) -> None:
        """
        Load the Annoy Index and Mapping from Disk

        This method loads the Annoy index and the dictionary mapping index positions to document chunks from disk.

        Args:
            name (str): The name used to generate the filenames for loading the index and dictionary.
        """
        ann_path = semantic_search.config.ANNOY_FOLDER/f"{name}.ann"
        convert_path = semantic_search.config.CONVERT_FOLDER/f"{name}.json"

        # Load the Annoy index
        self.annoy.load(str(ann_path))

        # Load the index_to_word dictionary
        with open(convert_path, 'r') as infile:
            self.index_to_word = json.load(infile)
            self.index_to_word = {int(key): value for key, value in self.index_to_word.items()}  # Convert keys back to integers
