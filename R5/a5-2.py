import sqlite3
from datetime import datetime
from flask import Flask, g, render_template

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.template_filter("datetimeformat")
def datetimeformat(value, format="%Y-%m-%d"):
    return datetime.strptime(value, format)


@app.route("/", methods=["GET"])
def database():
    db = get_db()
    cur = db.execute("SELECT * FROM events")
    all_events = cur.fetchall()

    cur = db.execute("SELECT * FROM events WHERE event_name LIKE '%オリンピック%'")
    olympic_events = cur.fetchall()

    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template(
        "a5-2.html",
        all_events=all_events,
        olympic_events=olympic_events,
        current_date=current_date,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
