# Rocketopoly -- "First Rocket Bank"
from flask import Flask, render_template, request
import csv
from pathlib import Path


# Init
app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PLAYER_CSV = BASE_DIR / "players.csv"




# Landing
@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/player")
def player():
    player = request.args.get("player")
    playerKey = player.lower().replace(" ", "")     # Changes i.e. Player 1 to player1
    
    banker = request.args.get("banker")
    if banker == "Yes":
        banker = True
    else:
        banker = False

    amount = getMoney(playerKey)
    return render_template(f"{playerKey}.html",
                                amount=amount,
                                player=player,
                                banker=banker)




# Helper functions
# Gets the amount of money a player has for the front-end UI
def getMoney(playerKey):
    # Opens the CSV, goes row by row
    with open(PLAYER_CSV, newline="", encoding="utf-8") as csvfile:
        csvMoney = csv.DictReader(csvfile)
        
        for row in csvMoney:
            # Grab the cell of the specific player, their money amount
            if row.get("player") == playerKey:
                return row.get("money")
            
    # Else return nothing if not found
    return None





# Run the App in debug mode for development, otherwise take it out
if __name__ == '__main__':
    app.run(debug=True)