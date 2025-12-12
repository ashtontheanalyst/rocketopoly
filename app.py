# Rocketopoly -- "First Rocket Bank"
from flask import Flask, render_template


# Init
app = Flask(__name__)




# Landing
@app.route("/")
def landing():
    return render_template("landing.html")




# Run the App in debug mode for development, otherwise take it out
if __name__ == '__main__':
    app.run(debug=True)