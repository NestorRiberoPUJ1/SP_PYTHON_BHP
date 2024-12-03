from flask_app import app

from flask_app.controllers import file_upload_controller

# Correr el servidor
if __name__ == '__main__':
    app.run(debug=True)
