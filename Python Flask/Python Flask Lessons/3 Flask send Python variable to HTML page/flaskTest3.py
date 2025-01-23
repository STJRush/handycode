# In this program, the major differences are:

# - We send the user to index.html. This MUST MUST be in a folder called templates


from flask import Flask, render_template # I've added the render_template library

app = Flask(__name__)


@app.route("/")
def home():
    
    # define your varaibles as normal
    pizza = "diabolo"
    health = 10
    jojo = 23
    
    # pass each variable on to your webpage (with a chance to rename them)
    return render_template("index.html", pizza=pizza, health=health, jojo=jojo) 


app.run(host='0.0.0.0', port=6001, debug=False)


"""
This is how your files need to be organised:

flask_app/
|-- app.py
|-- templates/
    |-- index.html

"""