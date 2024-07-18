from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

spring_s = datetime(2024, 4, 8)
spring_e = datetime(2024, 7, 19)
fall_s1 = datetime(2024, 9, 20)
fall_e1 = datetime(2024, 12, 23)
fall_s2 = datetime(2025, 1, 6)
fall_e2 = datetime(2025, 1, 9)


def sem(date):
    if spring_s <= date <= spring_e:
        return "春学期中"
    elif fall_s1 <= date <= fall_e1 or fall_s2 <= date <= fall_e2:
        return "秋学期中"
    else:
        return "授業期間外"


def countdown(date):
    if spring_s <= date <= spring_e:
        end_date = spring_e
    elif fall_s1 <= date <= fall_e1:
        end_date = fall_e1
    elif fall_s2 <= date <= fall_e2:
        end_date = fall_e2
    else:
        return None
    days_left = (end_date - date).days
    return days_left


@app.context_processor
def countdown_processor():
    def get_countdown(date):
        return countdown(date)

    return dict(countdown=get_countdown)


@app.route("/")
def index():
    return render_template("b3-2in.html")


@app.route("/result", methods=["POST"])
def result():
    input_date = request.form["date"]
    date_obj = datetime.strptime(input_date, "%Y-%m-%d")
    sem_status = sem(date_obj)
    days_left = countdown(date_obj)
    return render_template(
        "b3-2out.html", date=input_date, sem_status=sem_status, days_left=days_left
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
