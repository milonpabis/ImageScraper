from flask import Flask, request, render_template, send_file, redirect, url_for
from src.Web.settings import *
from src.Web.utils import *
import threading
from queue import Queue

app = Flask(__name__)
zip_storage = {} # storing the zip files in memory


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form.getlist("keywords[]")

        if any([True if keyword else False for keyword in data]):
            data = [keyword for keyword in data if keyword] # filtering out empty strings
            zip_file = compress_all(data) # compressing all the images to a zip file
            if zip_file:
                id = generate_unique_id()
                zip_storage[id] = zip_file
                return redirect(url_for("download_complete", zip_id=id))
    return render_template("home.html")


@app.route("/download/<zip_id>", methods=["GET"])
def download_complete(zip_id):
    global zip_storage
    zip_file = zip_storage.pop(zip_id, None) # getting the zip file from memory
    if zip_file:
        return send_file(zip_file, as_attachment=True, download_name=f"{zip_id}.zip")
    else:
        return "File not found", 404