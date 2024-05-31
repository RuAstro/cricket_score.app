from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """Cricket scoring app, to track score of the game. Makes scoring for coaches a lot easier and faster, so that there is not a 
            moment to miss on the field. Everything by just a click of buttons. The feature of app will be updated regally. The 
            idea of the app is to spare some time and have bit more outlook on whats happening on the field. And dont feel rush 
            for next tracking ball that follows. User can log in with same username and password, when register."""


if __name__ == "__main__":
    app.run(debug=True)
