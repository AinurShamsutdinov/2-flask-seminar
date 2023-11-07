from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pathlib import Path, PurePath

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/upload/')
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.joinpath(Path.cwd(), 'uploads', file_name)))
        return f'File {file_name} downloaded on server'
    return render_template('upload-image.html')


@app.post('/upload/')
def upload_file():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.joinpath(Path.cwd(), 'uploads', file_name)))
    return f'File {file_name} downloaded on server'


if __name__ == '__main__':
    app.run(debug=True)
