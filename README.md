# cricket_score.app
Cricket scoring app, to track score of the game.
Makes scoring for coaches alot easier and faster, so that there is not a moment to miss on the field. Everything by just a click of buttons.
The feuture of app will be updated regeurly.
The idee of the app is to spare some time and have bit more outlook on whats happening on the field. And dont feel rush for next tracking ball that follows.
User can log in with same username and password, when register.


## Requirements
- Program should take teams name.
- Take all 11 batsmen names in order.
- Have buttons for runs(1, 2, 3, 4, 5, 6) with the two batsmen facing the balls on the pitch
- Will also show strike rate from each batsmen through out the season.
- Buttons for ekstra runs, for exsample(wide, no ball, leg byes etc.)
- Will have a total of runs scoring as the game goes go on and runs added to the total.
- Have edit space for bowlers that are bowling currently to put in their names and balls they are bowling with the total runs that are being hitted by their name.(for each bowler their will be tracking average number of balls bowled per wicked taken)
- Will automatically work out the RR(run rate) and CRR(current run rate for batsmen)
- Can also make a log for the season for each leage that are participating in the season for each team.
- Will automatically declere winner after all batsmen are out, or when all runs are chased.

## Technical Requirements
- Built in python
- Using flask/django and jinja2 templates
- unit tests
- pre-commit checks enforced, linting, formatting etc
