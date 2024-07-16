import semantic_search

from semantic_search.parsers.txt import process_txt
from semantic_search.parsers.pdf import process_pdf

PARSER_MAP = {
    '.txt': process_txt,
    '.pdf': process_pdf,
}