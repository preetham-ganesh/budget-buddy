# Copyrights (c) 2023 Preetham Ganesh, Harsha Vardhini Vasu.


from flask_sqlalchemy import SQLAlchemy


# Creates an object for SQAlchemy class.
db = SQLAlchemy()


class User(db.Model):
    """Defines the structure & attributes of user data within a web application.

    Defines the structure & attributes of user data within a web application. Represents individual users who interact
        with the application.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
