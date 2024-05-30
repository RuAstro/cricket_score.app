from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def description():
    title = "The Flask Adventure"
    description_text = """
    Cricket scoring app, to track score of the game. Makes scoring for coaches alot easier and faster, so that there is not a 
    moment to miss on the field. Everything by just a click of buttons. The feuture of app will be updated regeurly. The 
    idee of the app is to spare some time and have bit more outlook on whats happening on the field. And dont feel rush 
    for next tracking ball that follows. User can log in with same username and password, when register.
    """
    return render_template(
        "description.html", title=title, description_text=description_text
    )


if __name__ == "__main__":
    app.run(debug=True)
