import sqlite3
from datetime import datetime
from flask import Flask, g, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = "a5-1.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    if request.method == "POST":
        event_name = request.form["event_name"]
        event_date = request.form["event_date"]
        location = request.form["location"]
        db.execute(
            "INSERT INTO events (event_name, event_date, location) VALUES (?, ?, ?)",
            (event_name, event_date, location),
        )
        db.commit()
        return redirect(url_for("index"))

    cur = db.execute("SELECT * FROM events")
    events = cur.fetchall()
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template("a5-3.html", events=events, current_date=current_date)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
