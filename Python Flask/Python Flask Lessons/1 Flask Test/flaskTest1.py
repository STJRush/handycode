# Copy paste into python (Thonny) to run this. 
# if you get "flask module not found", type CTRL+ T to run in terminal. Then type "pip install flask"
# if pip won't run, you need to install python from python.org (not the manager) and click the "Add to Path" box on install.

# Run the program and then click on the blue hyperlink IP address to open the webpage
# If this loads forever, try another port eg. 6002 and set debug to False
# after "Press CTRL+C to quit" you should see anther line in the console, something like
# 127.0.0.1 - - [09/Dec/2024 13:32:45] "GET / HTTP/1.1" 200 -
# Don't forget to stop the previous code. On the browser, hold ctrl and click refresh to clear the cache

from flask import Flask

# Let's flask know this is your main program, the one you clicked run on
app = Flask(__name__)

# The home page of your website is ('/'). We'll send this to index.html in the next lesson.
@app.route('/')
def home():
    return "Flask is working properly! Huzaah!"


# This tells flask to run the app on your computer's IP (in case others might want to connect to it)
app.run(host='0.0.0.0', port=6001, debug=False)
