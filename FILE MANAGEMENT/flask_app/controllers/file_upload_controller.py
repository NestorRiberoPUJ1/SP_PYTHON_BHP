import os
from flask import jsonify, request, send_file
from flask_app import app
from flask_app.utils.file_validation import allowed_file

from werkzeug.utils import secure_filename


@app.route('/profile-img', methods=['POST'])
def upload_profile_img():

    print(request.files)
    if 'profile_picture' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['profile_picture']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename, 'img'):
        return jsonify({'error': 'Invalid file extension'}), 400
    filename = secure_filename(file.filename)
    # SI NO EXISTE LA CARPETA UPLOADS, LA CREAMOS
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
       
    return jsonify({'message': 'File uploaded successfully','url':file_path}), 200


@app.route('/view-img/<filename>', methods=['GET'])
def view_img(filename):
    # COLOCAR TODA LA LÓGICA PARA SERVIR EL ARCHIVO	
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    serve_path = os.path.join(app.config['SERVE_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    return send_file(serve_path)