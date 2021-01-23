from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome</h1> Hello World! this is first main webpage in Python Flask"


@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
