# Semantic Search API

This project implements a semantic search API that allows users to upload documents, process them for semantic search, and query the processed documents. Semantic search goes beyond simple keyword matching, understanding the context and meaning of the query to provide more relevant results.

## Features

- Document upload and management
- Asynchronous document processing
- Semantic embedding of document chunks
- Fast approximate nearest neighbor search using ANNOY
- RESTful API for interacting with the system

## Getting Started

Clone the repository:

```
git clone git@github.com:hunterros-s/semantic-search-rest-api.git
cd semantic-search-rest-api
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Flask application

```
python3 semantic_search_server/run_debug.py
```

## API Endpoints

### Upload Documents
**URL**: ``/api/v1/upload/``

- ``GET``: Returns an HTML form for uploading files.
- ``POST``: Handles file uploads, saving them to the configured upload folder and adding their metadata to the corpus.

Example Request:
```
# From a command line (using cURL)
curl -X POST -F "file=@example.txt" http://localhost:5000/api/v1/upload/
```

Example Response:
```
[
  {
    "filename": "example.txt",
    "basename": "unique-identifier-example.txt",
    "path": "/path/to/uploads/unique-identifier-example.txt",
    "contents_hash": "file-content-sha256-hash",
    "status": "uploaded",
    "url": "/api/v1/corpus/unique-identifier-example.txt/"
  }
]
```

### View and Manage Document Corpus
**URL**: ``/api/v1/corpus/``

- ``GET``: Returns a JSON representation of the entire document corpus.

Example Request:
```
# From a command line (using cURL)
curl -X GET http://localhost:5000/api/v1/corpus/
```

Example Response:
```
{
  "unique-identifier-example.txt": {
    "filename": "example.txt",
    "basename": "unique-identifier-example.txt",
    "path": "/path/to/uploads/unique-identifier-example.txt",
    "contents_hash": "file-content-sha256-hash",
    "status": "uploaded",
    "url": "/api/v1/corpus/unique-identifier-example.txt/",
    "ANNOY_path": null,
    "convert_path": null
  },
  ...
}
```

### Document Information and Processing
**URL**: ``/api/v1/corpus/<basename>/``

- ``GET``: Retrieves metadata for a specific document in the corpus.

Example Request:
```
# From a command line (using cURL)
curl -X GET http://localhost:5000/api/v1/corpus/unique-identifier-example.txt/
```

Example Response:
```
{
  "filename": "example.txt",
  "basename": "unique-identifier-example.txt",
  "path": "/path/to/uploads/unique-identifier-example.txt",
  "contents_hash": "file-content-sha256-hash",
  "status": "uploaded",
  "url": "/api/v1/corpus/unique-identifier-example.txt/",
  "ANNOY_path": null,
  "convert_path": null
}
```

**URL**: ``/api/v1/corpus/<basename>/process``

- ``GET``: Initiates the asynchronous processing of the specified document.

Example Request:
```
# From a command line (using cURL)
curl -X GET http://localhost:5000/api/v1/corpus/unique-identifier-example.txt/process
```

Example Response:
```
{
  "status": "processing"
}
```

### Query Processed Documents
**URL**: ``/api/v1/query/``

- ``GET``: Lists all documents that are available for querying (i.e., those successfully processed and embedded).

**URL**: ``/api/v1/query/<hash>``

- ``GET``: Queries the specified document with a provided query string.

Example Request:
```
# From a command line (using cURL)
curl -X GET "http://localhost:5000/api/v1/query/file-content-sha256-hash?query=search%20term"
```

Example Response:
```
[
  ["Matching content snippet 1", 0.987],
  ["Matching content snippet 2", 0.965],
  ...
]
```

## Configuration

Adjust settings in `config.py` to customize paths and other parameters.

## Dependencies

- Flask
- sentence-transformers
- Annoy
- NLTK

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

```
MIT License

Copyright (c) 2024 Hunter Ross

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Future Improvements

- Support for more document types (PDF, DOCX, etc.)
- Improved chunking algorithms for better context preservation
- Integration with popular NLP models for enhanced semantic understanding