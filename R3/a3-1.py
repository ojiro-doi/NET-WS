from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def route():
    dt = datetime.now()

    if dt.second % 2 == 0:
        color = "blue"
    else:
        color = "red"

    return render_template(
        "a3-1.html",
        title="A3-1",
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        color=color,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
