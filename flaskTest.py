from flask import Flask, render_template, url_for, request, redirect
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greetings", methods=["POST"])
def hello():

    # get variables first then change form later
    name = request.form.get("inputName")
    lastName = request.form.get("inputLastName")
    name = name.capitalize()
    lastName = lastName.capitalize()

    # change form in else
    if request.method == "GET":
        return f"<h1>Please submit the form instead</h1>"
    else:
        return render_template("secondPage.html", name=name, lastName=lastName)


if __name__ == "__main__":
    app.run(debug=True)

