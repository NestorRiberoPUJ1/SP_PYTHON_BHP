from flask_app import app
from flask import render_template
from flask_app.models.users import Users


# RUTAS DE LA APLICACIÓN
@app.route('/users')
def users():
    user_list = Users.get_all()
    return render_template('users.html', users=user_list)
