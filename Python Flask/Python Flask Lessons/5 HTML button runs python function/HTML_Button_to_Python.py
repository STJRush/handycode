# if this loads forever, try another port eg. 6002 and set debug to False
# after "Press CTRL+C to quit" you should see anther line in the console, something like
# 127.0.0.1 - - [09/Dec/2024 13:32:45] "GET / HTTP/1.1" 200 -
# Don't forget to stop the previous code. On the browser, hold ctrl and click refresh to clear the cache

from flask import Flask, render_template # I've added the render_template library
from random import choice

app = Flask(__name__)


@app.route("/")
def home():
    
    # define your varaibles as normal
    pizza = "diabolo"
    health = 10
    
    # pass these on to your webpage (with a chance to rename them)
    return render_template("index.html", pizza=pizza, health=health)



@app.route("/boring")
def boring_page():
    
    # Define a list of boring things
    list_of_boring = ["Grey trousers", "Paperwork", "Reports", "People who are NPCs","People who have no opinions", "Surveys with more than 3 quesitons" ]
    
    # Pick one item from the list
    rando_boring_thing = choice(list_of_boring)
    
    # Print it here to check it works
    print(rando_boring_thing)
    
    # Send these variables to boring.html
    return render_template("boring.html", rando_boring_thing = rando_boring_thing)


@app.route("/button-clicked", methods=["POST"])
def button_clicked():
    # Perform some Python action
    print("Button was clicked!")
    # Optionally, redirect back to the homepage or another page
    return render_template("index.html", pizza="hawaiian", health=20)



app.run(host='0.0.0.0', port=6001, debug=False)


"""
This is how your files need to be organised:

flask_app/
|-- app.py
|-- templates/
    |-- index.html
    |-- boring.html

"""
