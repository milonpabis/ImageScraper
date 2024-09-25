import os
from pathlib import Path, WindowsPath
from src.Web.settings import *
import uuid
import io
from PIL import Image, UnidentifiedImageError
import zipfile
from typing import Iterable
from src.Models.scraper import Scraper


def run_process(keyword: str) -> io.BytesIO | None:
    """
    Runs a single instance of the scraper.
    """
    id = str(generate_unique_id()) # generating unique id for the folder
    create_dir_if_not_exists(id)
    scraper = Scraper()
    scraper.execute_and_encode(keyword, Path(TEMP_DIRECTORY) / id)

    image_folder = Path(TEMP_DIRECTORY) / id / keyword
    images_data = [image_to_bytes(image_folder / file_name) for file_name in os.listdir(image_folder) 
                        if is_image(image_folder / file_name)]  # converting images to bytes
    
    zip_data = compress_images(images_data) # compressing images from one keyword to a zip file

    return id, zip_data


def compress_images(images_data: Iterable[io.BytesIO]) -> io.BytesIO | None:
    """
    Compresses the whole folder of images to a zip file.
    """

    zip_data = io.BytesIO()
    try:
        with zipfile.ZipFile(zip_data, "w") as zipf:
            for image_data in images_data:
                if image_data:
                    zipf.writestr(f"{generate_unique_id()}.jpg", image_data.getvalue())
        zip_data.seek(0)
    except Exception as exception_zip_creation:
        print("ZIP :", exception_zip_creation)
        return None
    return zip_data


def image_to_bytes(image_path: str) -> io.BytesIO | None:
    """
    Converts an image to BytesIO. Also filters the images that are too small.
    """
    image_data = io.BytesIO()
    try:
        with Image.open(image_path).convert("RGB") as image:
            if image.width < MIN_IMAGE_WIDTH:
                return None
            image.save(image_data, format="JPEG")
        image_data.seek(0)
    except UnidentifiedImageError as exception_image_convert:
        print("IMAGE :", exception_image_convert)
        return None
    return image_data


def create_dir_if_not_exists(file_name: str) -> None:
    """
    Creates the directory for the downloads.
    """
    file_path = Path(TEMP_DIRECTORY) / file_name
    try:
        if not os.path.exists(file_path):   # creating a directory with main one if does not exist
            os.makedirs(file_path)
    except Exception as exception_mkdir:
        print(exception_mkdir)


def generate_unique_id() -> str:
    return str(uuid.uuid4())


def is_image(file_name: WindowsPath | str) -> bool:
    return str(file_name).endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))





    
