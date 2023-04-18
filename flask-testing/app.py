# ~~~~~~~~~~~~~~~~~~~~~~assert~~~~~~~~~~~~~~~~~~~~~
# helps promote modular code Test Driven Development TDD
# def adder(x, y):
#     """Add two numbers together"""

#     return x + y


# assert adder(2, 5) == 7
# assert adder(2, 7) == 10, "expected 2+7 to be 10"
# # won't run b/c ^ failed and raised an assertion error with break
# assert adder(2, 3) == 5

# can run without assert running, in terminal (but not ipy), python -O file.py
# assert is a statement, not a function, not passing arguments, statement to 'assert' (evaluate), and then an error string

# ~~~~~~~~~~~~~~~~~~~~~~~~doc tests~~~~~~~~~~~~~~~~~~~~~~~~~
# run in py, not ipy
# not a 'test' but an example of how it should work
# in py, from app import adder to play and test

# def adder(x, y):
#     """
#     Add two numbers together
#     >>> adder(3,5)
#     8
#     >>> adder(-1,50)
#     49
#     """

#     return x + y + 1

#~~~~~~~~~~~~~~~~~~~~~~~~~unittest~~~~~~~~~~~~~~~~~~~~
#bundle of tests
#starts with test_descriptivename
#python -m unittest NAME_OF_FILE runs all cases


# from unittest import TestCase

# def adder(x, y):
#     """
#     Add two numbers together
#     >>> adder(3,5)
#     8
#     >>> adder(-1,50)
#     49
#     """

#     return x + y + 1

# def reverse_str(s):
#     """Returns reverse of intput str (s)"""
#     return s[::-1]


# def is_palindrome(s):
#     """Boolean method to check weather given string is a palindrome"""
#     rev = reverse_str(s)
#     return s.lower() == rev.lower()


# def factorial(n):
#     """Calculates factorial iteratively"""
#     if not (isinstance(n, int) and n >= 0):
#         raise ValueError("n must be a non-negative integer")
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result

#~~~~~~~~~~~~~~~~~~~~~~~~~integration tests~~~~~~~~~~~~~~~~~~~~
from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.debug = True

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    """Show homepage"""

    # Keep a count of how many times page is visited
    session["count"] = session.get("count", 0) + 1

    return render_template("index.html")


@app.route("/fav-color", methods=["POST"])
def fav_color():
    """Show favorite color"""

    fav_color = request.form.get("color")

    return render_template("color.html", fav_color=fav_color)


@app.route("/redirect-me")
def redirect_me():
    """Redirect user to homepage"""

    return redirect("/")
