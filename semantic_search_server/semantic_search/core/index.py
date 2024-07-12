import semantic_search
from annoy import AnnoyIndex
import semantic_search.config
from semantic_search.core import embed
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
    
    def save(self, name: str) -> tuple[str, str]:
        ann_path = semantic_search.config.ANNOY_FOLDER/f"{name}.ann"
        self.annoy.save(str(ann_path))

        convert_path = semantic_search.config.CONVERT_FOLDER/f"{name}.json"
        with open(convert_path, 'w') as outfile:
            json.dump(self.index_to_word, outfile)
        
        return (ann_path, convert_path)
