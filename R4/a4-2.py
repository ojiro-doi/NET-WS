from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secretKey"


@app.route("/", methods=["GET", "POST"])
def index():
    if "x" not in session:
        session["x"] = 0
    return render_template("a4-2.html", x=session["x"])


@app.route("/calculate", methods=["POST"])
def calculate():
    if "x" not in session:
        session["x"] = 0

    x = session["x"]
    y = int(request.form["inputValue"])
    operation = request.form["operation"]

    if operation == "add":
        x += y
    elif operation == "subtract":
        x -= y
    elif operation == "multiply":
        x *= y
    elif operation == "divide":
        if y != 0:
            x /= y
        else:
            return "Error: Division by zero."

    session["x"] = x
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="localhost")
