from flask import Flask, request, jsonify, render_template, send_file, redirect, url_for
from src.Models.scraper import Scraper
from src.Web.settings import *
from src.Web.utils import *

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form.getlist("keywords[]")
        if any([True if keyword else False for keyword in data]):
            id = generate_unique_id()
            create_dir_if_not_exists(id)
            scraper = Scraper()
            scraper.execute_and_encode(data[0], Path("src/Web/tmp") / id)

            return redirect(url_for("download_file", file_name=id))



        
    return render_template("home.html")


@app.route("/download/<file_name>", methods=["GET"])
def download_file(file_name):
    return f"here you can download the file {file_name}"