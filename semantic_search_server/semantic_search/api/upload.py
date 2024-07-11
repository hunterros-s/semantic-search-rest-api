"""Upload related routes."""
import flask
import semantic_search
import uuid
import hashlib
import urllib.parse
import pathlib

import semantic_search.model

upload_html = """<html>   
<head>   
    <title>upload</title>   
</head>   
<body>   
    <form action="/api/v1/upload" method="post" enctype="multipart/form-data">   
        <input type="file" name="file" multiple />  
        <input type="submit" value="Upload">   
    </form>   
</body>   
</html>"""


@semantic_search.app.route('/api/v1/upload/', methods=['GET', 'POST'], strict_slashes=False)
def upload():
    if flask.request.method == "GET":
        return upload_html
    elif flask.request.method == "POST":

        files = flask.request.files.getlist("file")

        # Filter out any empty FileStorage objects
        files = [file for file in files if file.filename]

        # Abort if no files uploaded
        if not files:
            flask.abort(400)

        context = []

        for fileobj in files:

            # Access file contents
            file_contents = fileobj.read()
            
            sha256 = hashlib.sha256()
            sha256.update(file_contents)
            document_hash = sha256.hexdigest()

            # Reset file pointer to the beginning
            fileobj.seek(0)

            filename = fileobj.filename
            stem = uuid.uuid4().hex
            basename = f"{stem}{filename}"
            path = semantic_search.config.UPLOAD_FOLDER/basename

            fileobj.save(path)

            data = {
                "filename": filename,
                "basename": basename,
                "path": str(path),
                "contents_hash": document_hash,
                "status": "uploaded",
                "url": f"/api/v1/corpus/{urllib.parse.quote(basename)}/"
            }

            context.append(data)
            semantic_search.model.CORPUS[basename] = data

        return flask.jsonify(context)
