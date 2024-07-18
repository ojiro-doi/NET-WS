from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

events = [
    {"id": 1, "name": "東京オリンピック", "date": "2021-07-23", "location": "東京"},
    {"id": 2, "name": "北京オリンピック", "date": "2022-02-04", "location": "北京"},
    {
        "id": 3,
        "name": "ロンドンオリンピック",
        "date": "2012-07-27",
        "location": "ロンドン",
    },
    {
        "id": 4,
        "name": "リオデジャネイロオリンピック",
        "date": "2016-08-05",
        "location": "リオデジャネイロ",
    },
    {"id": 5, "name": "パリオリンピック", "date": "2024-07-26", "location": "パリ"},
    {
        "id": 6,
        "name": "ロサンゼルスオリンピック",
        "date": "2028-07-21",
        "location": "ロサンゼルス",
    },
    {
        "id": 7,
        "name": "カタールワールドカップ",
        "date": "2022-11-20",
        "location": "ドーハ",
    },
    {
        "id": 8,
        "name": "ロシアワールドカップ",
        "date": "2018-06-14",
        "location": "モスクワ",
    },
    {
        "id": 9,
        "name": "ブラジルワールドカップ",
        "date": "2014-06-12",
        "location": "リオデジャネイロ",
    },
    {
        "id": 10,
        "name": "アメリカ・カナダ・メキシコワールドカップ",
        "date": "2026-06-08",
        "location": "ニューヨーク",
    },
]


@app.route("/")
def index():
    today = datetime.now().date()
    events_with_future_flag = [
        {
            "id": event["id"],
            "name": event["name"],
            "date": event["date"],
            "location": event["location"],
            "is_future": datetime.strptime(event["date"], "%Y-%m-%d").date() > today,
        }
        for event in events
    ]
    return render_template("b3-1.html", events=events_with_future_flag)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
