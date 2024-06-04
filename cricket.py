from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Calculation of Run Rate..."


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        runs = int(request.form["runs"])
        overs = int(request.form["overs"])
        run_rate = calculate_run_rate(runs, overs)
        return render_template("result.html", run_rate=run_rate)
    return render_template("calculate.html")


def calculate_run_rate(runs, overs):
    return runs / overs


if __name__ == "__main__":
    app.run(debug=True)
