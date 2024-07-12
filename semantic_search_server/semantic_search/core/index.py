import semantic_search
from annoy import AnnoyIndex
import semantic_search.config
from semantic_search.core import embed, embed_query
import json 

class Index:
    def __init__(self) -> None:
        self.annoy = AnnoyIndex(semantic_search.config.EMBEDDING_SIZE, 'angular')
        self.index_to_word = {}
    
    def apply_chunks(self, chunks: list[str]) -> None:
        for idx, chunk in enumerate(chunks):
            self.index_to_word[idx] = chunk
    
    def embed(self) -> None:
        embeddings = embed(list(self.index_to_word.values()))

        for idx, embedding in enumerate(embeddings):
            self.annoy.add_item(idx, embedding)
        
        self.annoy.build(100)
    
    def query(self, text):
        query_embedding = embed_query(text)

        result_indicies = self.annoy.get_nns_by_vector(query_embedding, 100, include_distances=True)

        result_idxs, scores = (result_indicies[0], result_indicies[1])

        results = [self.index_to_word[i] for i in result_idxs]

        output = list(zip(results, scores))

        return output

    
    def save(self, name: str) -> tuple[str, str]:
        ann_path = semantic_search.config.ANNOY_FOLDER/f"{name}.ann"
        self.annoy.save(str(ann_path))

        convert_path = semantic_search.config.CONVERT_FOLDER/f"{name}.json"
        with open(convert_path, 'w') as outfile:
            json.dump(self.index_to_word, outfile)
        
        return (ann_path, convert_path)  

    def load(self, name: str) -> None:
        ann_path = semantic_search.config.ANNOY_FOLDER/f"{name}.ann"
        convert_path = semantic_search.config.CONVERT_FOLDER/f"{name}.json"

        # Load the Annoy index
        self.annoy.load(str(ann_path))

        # Load the index_to_word dictionary
        with open(convert_path, 'r') as infile:
            self.index_to_word = json.load(infile)
            self.index_to_word = {int(key): value for key, value in self.index_to_word.items()}  # Convert keys back to integers
