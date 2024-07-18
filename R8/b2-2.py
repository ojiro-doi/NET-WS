from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("b3-1.html")


@app.route("/countdown", methods=["POST"])
def countdown():
    event_name = request.form["event-name"]
    event_date = request.form["event-date"]

    event_date_obj = datetime.datetime.strptime(event_date, "%Y-%m-%d")
    today = datetime.datetime.today()
    days_diff = (today - event_date_obj).days

    message = f"{event_name}[{event_date}]まであと{days_diff}日です．"
    return render_template("b2-2.html", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
