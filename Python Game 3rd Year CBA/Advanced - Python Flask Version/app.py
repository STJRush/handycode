from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for sessions

# Route to reset game and start at the beach
@app.route("/")
def index():
    # Reset game state
    session['bag'] = []             # Player's inventory
    session['dragonHealth'] = 10    # Dragon's health in secret room
    session['playerHealth'] = 10    # Player's health in secret room
    return redirect(url_for('beach'))

# Beach location: add random loot and show options
@app.route("/beach")
def beach():
    bag = session.get('bag', [])
    # List of possible items at the beach
    loot_list = ["gold", "eggs", "old key"]
    loot = random.choice(loot_list)
    bag.append(loot)
    session['bag'] = bag
    return render_template("beach.html", bag=bag)

# Forest location: show available moves
@app.route("/forest")
def forest():
    return render_template("forest.html")

# Mountains location: check for key and show options
@app.route("/mountains")
def mountains():
    bag = session.get('bag', [])
    # If the player has the key, automatically go to the secret room
    if "old key" in bag:
        return redirect(url_for('secret_room'))
    return render_template("mountains.html")

# Secret Room location: combat with the dragon
@app.route("/secret_room", methods=["GET", "POST"])
def secret_room():
    if request.method == "POST":
        attack = request.form.get("attack")
        dragonHealth = session.get('dragonHealth', 10)
        playerHealth = session.get('playerHealth', 10)
        message = ""
        
        if attack == "s":
            damage = random.randint(1, 10)
            dragonHealth -= damage
            message += f"You use a sword attack. The dragon takes {damage} damage. "
        elif attack == "b":
            damage = random.randint(2, 3)
            dragonHealth -= damage
            message += f"You throw your boot. The dragon takes {damage} damage. "
        else:
            message += "Invalid action. No damage done. "
        
        # Dragon's turn if it is still alive
        if dragonHealth > 0:
            d_damage = random.randint(2, 6)
            playerHealth -= d_damage
            message += f"The dragon uses MORNING BREATH and deals {d_damage} damage to you."
        
        session['dragonHealth'] = dragonHealth
        session['playerHealth'] = playerHealth

        # Check for win/loss
        if playerHealth <= 0:
            return redirect(url_for('death'))
        if dragonHealth <= 0:
            return redirect(url_for('victory'))
        
        return render_template("secret_room.html", message=message,
                               playerHealth=playerHealth, dragonHealth=dragonHealth)
    else:
        # GET request: show the initial secret room combat page
        dragonHealth = session.get('dragonHealth', 10)
        playerHealth = session.get('playerHealth', 10)
        return render_template("secret_room.html", message="",
                               playerHealth=playerHealth, dragonHealth=dragonHealth)

# Death page
@app.route("/death")
def death():
    return render_template("death.html")

# Victory page
@app.route("/victory")
def victory():
    return render_template("victory.html")

if __name__ == "__main__":
    app.run(debug=False, port = 5007)

