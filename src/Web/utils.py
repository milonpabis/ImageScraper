import os
from pathlib import Path
from src.Web.settings import *
import uuid

def create_dir_if_not_exists(file_name: str) -> None:
    file_path = Path(TEMP_DIRECTORY) / file_name
    try:
        if not os.path.exists(file_path):   # creating a directory with main one if does not exist
            os.makedirs(file_path)
    except Exception as exception_mkdir:
        print(exception_mkdir)

def generate_unique_id() -> str:
    return str(uuid.uuid4())





    
