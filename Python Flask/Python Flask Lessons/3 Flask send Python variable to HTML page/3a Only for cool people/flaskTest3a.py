# In this program, the major differences are:

# - We send the user to index.html. This MUST MUST be in a folder called templates


from flask import Flask, render_template # I've added the render_template library

app = Flask(__name__)


@app.route("/")
def home():
    
    # define your local varaibles as normal inside your function
    
    pizza = "diabolo"
    health = 10
    armour = 18
    charisma = 20
    gold = 10000000
    power_level = 9001
    
    # pass ALL local variables on to your webpage like a boss. No need for health == health 
    return render_template("index.html", **locals())


app.run(host='0.0.0.0', port=6001, debug=False)


"""
This is how your files need to be organised:

flask_app/
|-- app.py
|-- templates/
    |-- index.html

"""