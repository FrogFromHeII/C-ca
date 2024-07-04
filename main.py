from flask import Flask, render_template

app = Flask(__name__)

# Hlavní stránka
@app.route("/")
@app.route('/uvod')
def uvodniStranka():
    return render_template("index.html")