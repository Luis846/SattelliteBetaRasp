from flask import Flask


app = Flask(__name__)

@app.route("/platinum")
def get_p_subscription():
    file = open('platinum.json', "r")
    text = file.read()
    contents = text.rstrip(",")
    contents = "[" + contents + "]"
    print("I am being called right now")
    return contents



