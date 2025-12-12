# Rocketopoly
Making monopoly better than it already was... and of course, a whole lot faster!

## Reasoning:
- Problem: Dealing with the physical money in monopoly is a pain in the rear for the banker
so let's put it online and easy to integrate into a physical game.
- Main Idea: **First Rocket Bank** is the online bank for my monopoly world. One user comes into
the game a selects to be the banker, then everyone else comes in as a regular player. When
a player needs to buy a property, pay a player, build a house, or etc. they make a request in
the app, every player is notified they are taking that action, then the banker approves or
denies the request (keeping accountability "accross the board"). If the banker approves the
action, the user gets a confirmation and then their balance is updated. On the bankers screen,
nothing will really change, they just act as an approving authority for transactions. 
- Idea (player to player): When a player needs to pay another player for rent or other reasons. This
type of transaction does not necessarily need to go through the bank, instead the player paying the
other will initiate that specific action, the receiver will approve or deny the action, then if
approved the payer will get a confirmation, and both players balances will update to reflect.

## Ideas:
- Make a landing page where players can select which player they want to be (more to follow on players)
and then make one html page for the player, another for the banker, and change the CSS of the page based
on the player. So we could associate plater "Scottie" with the color blue, when a player selects "Scottie"
they go to the same layout page as every other regular player, but the accents are all blue and distinguishable.
- Should the players be 1-8 (that's the max in basic monopoly rules), A,B,C..., Blue, Green, Red... or
something else?

## Development Setup:
```sh
# Creating venv
py -m venv rocketenv

# Activating
.\rocketenv\Scripts\activate        # windows
source rocketenv/bin/activate       # linux

# Downloading packages
pip install -r requirements.txt
```