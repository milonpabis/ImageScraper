from flask import Flask, request, render_template, send_file
from src.Web.settings import *
from src.Web.utils import *

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form.getlist("keywords[]")

        if any([True if keyword else False for keyword in data]):
            id, zip_data = run_process(data[0])

            print("sending file")
            return send_file(zip_data, as_attachment=True, download_name=f"{id}.zip") # getting the file to the user

    return render_template("home.html")