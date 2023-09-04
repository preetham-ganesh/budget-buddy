# Copyrights (c) 2023 Preetham Ganesh, Harsha Vardhini Vasu.


from flask_sqlalchemy import SQLAlchemy
import re


# Creates an object for SQAlchemy class.
db = SQLAlchemy()


class User(db.Model):
    """Defines the structure & attributes of user data within a web application.

    Defines the structure & attributes of user data within a web application. Represents individual users who interact
        with the application.
    """

    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


def validate_email_id(email_id: str) -> bool:
    """Checks the validity of the email_id.

    Checks the validity of the email_id.

    Args:
        email_id: A string for email_id which needs validation.

    Returns:
        A boolean value for the validity of the email_id, i.e., true if valid, and false if invalid.
    """
    # Checks type of arguments.
    assert isinstance(email_id, str), "Argument email_id should be of type 'str'."

    # Checks if the string text is a valid email.
    if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", email_id):
        return True
    else:
        return False
