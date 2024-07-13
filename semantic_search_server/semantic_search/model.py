"""
Handles Corpus

This module defines the `CorpusManager` class for managing the document corpus. The `CorpusManager` is responsible for
loading, saving, and modifying the corpus data stored in a JSON file. It includes methods to retrieve, set, and check
for items in the corpus, as well as converting the corpus to a dictionary format.
"""
import flask
import semantic_search
import os
import json


class CorpusManager:
    def __init__(self, json_file):
        self.json_file = json_file
        self.corpus = self.load_corpus()

    def load_corpus(self):
        """Load the corpus from JSON file if exists."""
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                return json.load(f)
        else:
            print("corpus.json not found")
            return {}

    def save_corpus(self):
        """Save current corpus information to JSON."""
        with open(self.json_file, 'w') as f:
            json.dump(self.corpus, f)

    def __getitem__(self, key):
        """Retrieve an item from the corpus."""
        return self.corpus[key]

    def __setitem__(self, key, value):
        """Set an item in the corpus and automatically save."""
        self.corpus[key] = value
        self.save_corpus()
    
    def to_dict(self):
        """Return the corpus as a dictionary."""
        return self.corpus

    def __contains__(self, key):
        """Check if a key exists in the corpus."""
        return key in self.corpus


CORPUS = CorpusManager(semantic_search.config.CORPUS_JSON)
