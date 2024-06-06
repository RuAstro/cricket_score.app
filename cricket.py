from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# logging.basicConfig(
#     filename="app.log",
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(message)s",
# )


@app.route("/")
def home():
    return """
    <h1>Cricket Score Calculation</h1>
    <p>Click the button below to calculate the run rate:</p>
    <form method="get" action="/calculate">
        <button type="submit">Calculate Run Rate</button>
    </form>
    
    <br>
    
    <h2>Cricket Batsmen Strike Rate Calculation</h2>
    <form method="post" action="/calculate_batsmen_strike_rate">
        Runs: <input type="text" name="runs"><br>
        Balls Faced: <input type="text" name="balls_faced"><br>
        <button type="submit">Calculate Batsmen Strike Rate</button>
    </form>
    
    <br>
    
    <h2>Cricket Bowler Strike Rate Calculation</h2>
    <form method="post" action="/calculate_bowler_strike_rate">
        Runs: <input type="text" name="runs"><br>
        Balls Bowled: <input type="text" name="balls_bowled"><br>
        <button type="submit">Calculate Bowler Strike Rate</button>
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
        return render_template(
            "result.html", run_rate=run_rate, required_run_rate=required_run_rate
        )
    return render_template("calculate.html")


@app.route("/calculate_batsmen_strike_rate", methods=["POST"])
def calculate_batsmen_strike_rate():
    runs = int(request.form["runs"])
    balls_faced = int(request.form["balls_faced"])
    batsmen_strike_rate = (runs / balls_faced) * 100
    return f"<h2>Strike Rate: {batsmen_strike_rate:.2f}</h2>"


@app.route("/calculate_bowler_strike_rate", methods=["POST"])
def calculate_bowler_strike_rate():
    runs = int(request.form["runs"])
    balls_bowled = int(request.form["balls_bowled"])
    bowler_strike_rate = (runs / balls_bowled) * 100
    return f"<h2>Strike Rate: {bowler_strike_rate:.2f}</h2>"


def calculate_run_rate(runs, overs, target_runs, remaining_overs):
    current_run_rate = runs / overs
    required_run_rate = (target_runs - runs) / remaining_overs
    return current_run_rate, required_run_rate


if __name__ == "__main__":
    app.run(debug=True)
