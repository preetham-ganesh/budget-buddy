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


def validate_username(username: str) -> bool:
    """Checks the validity of the username.

    Checks the validity of the username.

    Args:
        username: A string for the username which needs to be validated.

    Returns:
        A boolean value for the validity of the username, i.e., true if valid, and false if invalid.
    """
    # Checks type of arguments.
    assert isinstance(username, str), "Argument username should be of type 'str'."

    # Checks if the string text is a valid email.
    if re.match("^[a-zA-Z0-9]*$", username):
        return True
    else:
        return False
