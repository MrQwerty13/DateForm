from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def page1():
    return render_template("page1.html")


@app.route("/page2", methods=["GET", "POST"])
def page2():
    return render_template("page2.html")


@app.route("/page3", methods=["GET", "POST"])
def page3():
    return render_template("page3.html")


@app.route("/submit", methods=["POST"])
def submit():
    date = request.form.get("date")
    place = request.form.get("place")

    print(f"Date: {date}")
    print(f"Place: {place}")

    return render_template(
        "success.html",
        date=date,
        place=place
    )


if __name__ == "__main__":
    app.run(debug=True)