"""Development config."""
import pathlib
import os
import semantic_search

APPLICATION_ROOT = pathlib.Path('/')

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
UPLOAD_FOLDER = ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

CORPUS_JSON = ROOT/'var'/'corpus.json'

# Ensure the directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

