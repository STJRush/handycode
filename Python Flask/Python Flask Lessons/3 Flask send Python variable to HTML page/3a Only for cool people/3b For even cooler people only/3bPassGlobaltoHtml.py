# not recommended for larger projects but you know... Safety third! (First fun, then danger)


# With this trick, you can use global variables that are not even in any function.
pizza = "diabolo"
health = 10
armour = 18
charisma = 20
gold = 10000000
power_level = 9001


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Pass all global variables to the template
    return render_template("index.html", **globals())

app.run(host='0.0.0.0', port=6001, debug=False)

# * First fun, then danger.