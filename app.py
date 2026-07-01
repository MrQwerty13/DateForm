import os

from flask import Flask, render_template, request

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
    # Получаем данные из формы
    date = request.form.get("date")
    place = request.form.get("place")

    # Записываем данные в файл data.txt
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Место: {place}\n")

    return render_template(
        "success.html",
        date=date,
        place=place
    )


if __name__ == "__main__":
    ip_address = "192.168.1.86"

    app.run(
        debug=False,
        host=ip_address,
        port=int(os.environ.get("PORT", 6767))
    )