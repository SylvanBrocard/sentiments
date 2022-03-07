from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Bienvenue chez moi</p>"

app.run()