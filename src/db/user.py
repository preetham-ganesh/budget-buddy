# Copyrights (c) 2023 Preetham Ganesh, Harsha Vardhini Vasu.


from flask_sqlalchemy import SQLAlchemy
import re


# Creates an object for SQAlchemy class.
user_db = SQLAlchemy()


class User(user_db.Model):
    """Defines the structure & attributes of user data within a web application.

    Defines the structure & attributes of user data within a web application. Represents individual users who interact
        with the application.
    """

    id = user_db.Column(user_db.Integer, primary_key=True)
    email_id = user_db.Column(user_db.String(120), unique=True, nullable=False)
    username = user_db.Column(user_db.String(16), unique=True, nullable=False)
    password = user_db.Column(user_db.String(120), nullable=False)
