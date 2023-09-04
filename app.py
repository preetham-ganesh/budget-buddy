# Copyrights (c) 2023 Preetham Ganesh, Harsha Vardhini Vasu.


import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)


from flask import Flask, render_template, request, flash, redirect, url_for
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


@app.route("/signup", methods=["GET", "POST"])
def signup() -> str:
    """Renders template for 'signup.html', and registers user into the database.

    Renders template for 'signup.html', and registers user into the database.

    Args:
        None.

    Returns:
        A string for the rendered template for 'signup.html'.
    """
    # If request method is 'post', then registers user to the application.
    if request.method == "POST":
        email_id = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        # Checks the validity of the email_id.
        if not validate_email_id(email_id):
            flash("- Invalid Email ID.", "error")

        # Checks the validity of the username.
        if not validate_username(username):
            flash("- Invalid username. (Use alphanumeric characters)", "error")

        # Check if the email is already registered in the database. If yes, then redirects to login.
        if User.query.filter_by(email_id=email_id).first():
            flash("- Email ID is already registered.", "error")

        else:
            # Create a new user using entered information.
            new_user = User(email_id=email_id, username=username, password=password)
            user_db.session.add(new_user)
            user_db.session.commit()
            return redirect(url_for("signup"))
    return render_template("signup.html")


if __name__ == "__main__":
    print()
    app.run(host="0.0.0.0", port=3000, debug=True)
