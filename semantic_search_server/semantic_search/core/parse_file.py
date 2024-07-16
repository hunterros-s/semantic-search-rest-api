"""
File Parsing for Semantic Search

This module provides a function for parsing files and extracting meaningful chunks of text. It currently supports
parsing text files (.txt) but can be extended to handle other file types.
"""
import flask
import semantic_search
from pathlib import Path

from semantic_search.parsers import PARSER_MAP


def parse_file(path):
    """
    Parses a file and returns chunks of its content.
    
    Args:
        path (str or Path): The path to the file to be parsed.
        
    Returns:
        list: A list of chunks from the file content.
        
    Raises:
        ValueError: If the file type is not .txt.
        IOError: If the file cannot be read.
    """
    path = Path(path)

    extension = path.suffix

    parser = PARSER_MAP.get(extension)
    if parser is None:
        raise ValueError(f"Unsupported file type: {extension}")

    return parser(path)