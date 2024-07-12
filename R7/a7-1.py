from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "a7-1.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    events = cur.fetchall()
    return render_template("a7-1.html", events=events)


@app.route("/search/event_name", methods=["GET"])
def search_event_name():
    event_name = request.args.get("event_name")
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM events WHERE event_name LIKE ?", ("%" + event_name + "%",)
    )
    events = cur.fetchall()
    return render_template("a7-1.html", events=events)


@app.route("/search/date", methods=["GET"])
def search_date():
    year = request.args.get("year")
    month = request.args.get("month")
    day = request.args.get("day")
    date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events WHERE event_date = ?", (date,))
    events = cur.fetchall()
    return render_template("a7-1.html", events=events)


@app.route("/search/location", methods=["GET"])
def search_location():
    location = request.args.get("location")
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events WHERE location LIKE ?", ("%" + location + "%",))
    events = cur.fetchall()
    return render_template("a7-1.html", events=events)


@app.route("/delete", methods=["POST"])
def delete_event():
    event_id = request.form["event_id"]
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
    conn.commit()
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add_event():
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    location = request.form["location"]
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO events (event_date, event_name, location) VALUES (?, ?, ?)",
        (event_date, event_name, location),
    )
    conn.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
