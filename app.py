# Copyrights (c) 2023 Preetham Ganesh, Harsha Vardhini Vasu.


import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)


from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import secrets
import string


from src.db.user_registration import user_db, User, validate_email_id, validate_username


# Initializes flask app.
app = Flask(__name__)

# Initialize and configures the database.
home_directory_path = os.getcwd()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.getcwd(), "db", "user.db"
)
user_db.init_app(app)

# Using the flask app object, creates the databases.
with app.app_context():
    user_db.create_all()

# Generates secret key for the flask app.
secret_key_length = 24
app.secret_key = "".join(
    secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    for _ in range(24)
)


if __name__ == "__main__":
    print()
    app.run(host="0.0.0.0", port=3000, debug=True)
