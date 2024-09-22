from flask import Flask, request, jsonify, render_template, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")