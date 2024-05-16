from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def table():
    schema = ["ID", "名称", "日時", "場所"]
    # 表の属性名のリスト
    table = [
        [1, "入学式", "2022/4/1", "上ヶ原キャンパス"],
        [2, "ネットワーク実習", "2024/4/11", "三田キャンパス"],
        [3, "卒業式", "2026/3/1", "上ヶ原キャンパス"],
    ]
    # 表の属性値のリスト
    return render_template("a3-2.html", title="教員名簿", schema=schema, table=table)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
