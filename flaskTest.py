from flask import Flask, render_template, url_for, request, redirect
import datetime

app = Flask(__name__)


# two methods will be used in this route, by default, FLASK will run get
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        # request info from variable nm
        user = request.form["nm"]
        password = request.form["pwd"]

        return redirect(url_for("users", usr=user, pwd=password))
    else:
        return render_template("index.html")


#positional args = 2
@app.route("/<usr>/<pwd>")
def users(usr, pwd):
    return f"<h1>{usr}</h1> <h2>{pwd}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
