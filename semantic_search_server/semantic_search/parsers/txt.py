import semantic_search

from semantic_search.utils import chunk

def process_txt(path):
    with open(path, 'rb') as file:
        text = file.read().decode('latin-1')

    chunks = chunk(text)

    return chunks