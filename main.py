from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

to_do_list = []


@app.route("/")
def home():
    return render_template("index.html", to_do_list=to_do_list)


@app.route("/add", methods=["POST"])
def add():
    to_do = request.form.get("to_do")
    to_do_list.append({"task": to_do, "completed": False})
    return redirect(url_for("home"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    to_do = to_do_list[index]
    if request.method == "POST":
        to_do["task"] = request.form.get("to_do")
        return redirect(url_for("home"))
    return render_template("edit.html", to_do=to_do, index=index)


@app.route("/delete/<int:index>", methods=["GET", "POST"])
def delete(index):
    to_do_list.pop(index)
    return redirect(url_for("home"))


@app.route("/check/<int:index>")
def check(index):
    to_do_list[index]["completed"] = not to_do_list[index]["completed"]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
