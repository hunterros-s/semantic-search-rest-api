"""
Text Processing Utilities

This module provides utility functions for processing text, specifically for splitting text into meaningful
chunks. It uses NLTK's sentence tokenizer to break text into sentences and then groups these sentences
into windows of three consecutive sentences.
"""
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def chunk(input):
    """
    Split Input Text into Chunks of Sentences

    This function takes an input text string, tokenizes it into sentences, and groups the sentences
    into windows of three consecutive sentences. If the input contains fewer than three sentences,
    it handles each case accordingly.

    Args:
        input (str): The input text string to be split into chunks.

    Returns:
        list[str]: A list of text chunks, each containing up to three consecutive sentences.
    """
    sentences = sent_tokenize(input)
    windowed_sentences = []

    # Check the number of sentences and handle accordingly
    if len(sentences) >= 3:
        # Zip sentences into groups of three consecutive sentences
        zipped_sentences = zip(sentences[:-2], sentences[1:-1], sentences[2:])
        # Join each group of three sentences into a single string
        windowed_sentences = [" ".join(window) for window in zipped_sentences]
    else:
        # If there are fewer than three sentences, handle each case
        if len(sentences) == 2:
            windowed_sentences.append(" ".join(sentences))
        elif len(sentences) == 1:
            windowed_sentences.append(sentences[0])

    return windowed_sentences