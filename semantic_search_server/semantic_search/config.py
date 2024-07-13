"""
Development Configuration for Semantic Search Application

This module contains the configuration settings for the development environment of the semantic search application. 
It defines various paths and constants used throughout the project, ensuring that necessary directories and files are in place.

Configuration Variables:
- `APPLICATION_ROOT`: The root path of the application.
- `ROOT`: The absolute path to the project's root directory, resolved from the location of this config file.
- `UPLOAD_FOLDER`: Directory path where uploaded files will be stored.
- `CORPUS_JSON`: Path to the JSON file where information about the document corpus is stored.
- `ANNOY_FOLDER`: Directory path where ANNOY index files will be stored.
- `CONVERT_FOLDER`: Directory path where the index to chunk conversion files are stroed.
- `EMBEDDING_SIZE`: Integer value defining the size of embeddings used in the model.

Initialization:
- Ensures that the `UPLOAD_FOLDER`, `ANNOY_FOLDER`, and `CONVERT_FOLDER` directories exist. If they do not exist, the directories are created.
"""
import pathlib
import os
import semantic_search

APPLICATION_ROOT = pathlib.Path('/')

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
UPLOAD_FOLDER = ROOT/'var'/'uploads'

CORPUS_JSON = ROOT/'var'/'corpus.json'

ANNOY_FOLDER = ROOT/'var'/'ANNOY'
CONVERT_FOLDER = ROOT/'var'/'convert'

EMBEDDING_SIZE = 768

# Ensure the directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ANNOY_FOLDER, exist_ok=True)
os.makedirs(CONVERT_FOLDER, exist_ok=True)
