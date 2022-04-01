import sqlite3
from flask import Flask
from views import views
import secrets, sqlalchemy


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

#SECRET_KEY
app.secret_key = secrets.token_urlsafe(16)

if __name__ == '__main__':
    app.run(debug=True, port=8000)