from flask import Flask, request, render_template
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.route("/")
def home():
    return """
    <h1>Cricket Score calculation</h1>
    <p>Click the button below to calculate the rates:</p>
    <form method="get" action="/calculate">
        <button type="submit">Calculate Run Rate</button>
    </form>
    """


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        runs = int(request.form["runs"])
        overs = int(request.form["overs"])
        target_runs = int(request.form["target_runs"])
        remaining_overs = int(request.form["remaining_overs"])
        run_rate, required_run_rate = calculate_run_rate(
            runs, overs, target_runs, remaining_overs
        )
        app.logger.info("Calculation successful")
        return render_template(
            "result.html", run_rate=run_rate, required_run_rate=required_run_rate
        )
    return render_template("calculate.html")


def calculate_run_rate(runs, overs, target_runs, remaining_overs):
    current_run_rate = runs / overs
    required_run_rate = (target_runs - runs) / remaining_overs
    return current_run_rate, required_run_rate


if __name__ == "__main__":
    app.run(debug=True)
