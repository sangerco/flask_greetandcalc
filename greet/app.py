from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    "create welcome page"

    html = """
        <h1>Welcome</h1>
    """
    return html

@app.route("/welcome/home")
def welcome_home():
    "create welcome home page"

    html = """
        <h1>Welcome Home</h1>
    """
    return html

@app.route("/welcome/back")
def welcome_back():
    "create welcome back page"

    html = """
        <h1>Welcome Back</h1>
    """
    return html