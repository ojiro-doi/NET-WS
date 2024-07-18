from flask import Flask, render_template, request

app = Flask(__name__)

# 両替レート（仮の値）
exchange_rates = {"USD": 110.0, "EUR": 130.0, "THB": 4.35}


@app.route("/")
def index():
    return render_template("b2-1in.html")


@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form["currency"]
    amount = float(request.form["amount"])
    rate = exchange_rates[currency]
    result = amount * rate
    return render_template(
        "b2-1out.html", currency=currency, amount=amount, result=result
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8000)
