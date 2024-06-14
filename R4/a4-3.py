from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


def read_events(file_path):
    events = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            date_str, event_name = line.strip().split(", ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            events.append((date, event_name))
    return events


@app.route("/")
def show_events():
    events = read_events("a4-3.txt")
    current_date = datetime.now().date()
    return render_template("a4-3.html", events=events, current_date=current_date)


if __name__ == "__main__":
    app.run(host="localhost")
