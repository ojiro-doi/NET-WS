from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def display_events():
    return render_template("a6-1.html")


if __name__ == "__main__":
    app.run(host="localhost")
