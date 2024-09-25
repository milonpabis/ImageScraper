from flask import Flask, request, render_template, send_file
from src.Models.scraper import Scraper
from src.Web.settings import *
from src.Web.utils import *
import zipfile
from PIL import Image, UnidentifiedImageError
import io

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form.getlist("keywords[]")
        if any([True if keyword else False for keyword in data]):
            id = generate_unique_id()
            download_folder = Path("src/Web/tmp")
            create_dir_if_not_exists(id)
            scraper = Scraper()
            scraper.execute_and_encode(data[0], download_folder / id)

            zip_filename = f"{id}.zip"

            print("Creating zip file")
            zip_data = io.BytesIO()
            try:
                with zipfile.ZipFile(zip_data, "w") as zipf:
                    for _, _, files in os.walk(download_folder / id):
                        images_bytes = io.BytesIO()
                        for file in files:
                            try:
                                image_full_path = download_folder / id / data[0] / file
                                with Image.open(image_full_path).convert("RGB") as image_data:
                                    if image_data.width < 10:
                                        print("Image too small", file)
                                        continue
                                    image_data.save(images_bytes, format="JPEG")
                                images_bytes.seek(0)
                            except UnidentifiedImageError:
                                continue
                            zipf.writestr(file, images_bytes.getvalue())
                zip_data.seek(0)
                print("Zip file created", zip_filename)
                return send_file(zip_data, as_attachment=True, download_name=f"{id}.zip")
            except Exception as exception_zip_creation:
                print("ZIP failed", exception_zip_creation)

            #return redirect(url_for("download_file", file_name=zip_filename[:-4]))  
    return render_template("home.html")