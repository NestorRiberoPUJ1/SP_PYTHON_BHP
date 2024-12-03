
from flask_app import ALLOWED_EXTENSIONS


def allowed_file(filename, type):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[type]
