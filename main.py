from src.DesktopApplication import DesktopApplication
from src.Web.app import app
from src.Web.utils import create_dir_if_not_exists, generate_unique_id

MODE = 0 # 0 - webapp, 1 - desktopapp, 2 - testing

if __name__ == "__main__":
    if MODE == 0:
        app.run(debug=True)
    elif MODE == 1:
        desktop_app = DesktopApplication()
        desktop_app.run()
    else:
        print(generate_unique_id())
        








