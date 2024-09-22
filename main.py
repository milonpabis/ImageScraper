from src.DesktopApplication import DesktopApplication
from src.Web.app import app

webapp = True

if __name__ == "__main__":
    if webapp:
        app.run(debug=True)
    else:
        desktop_app = DesktopApplication()
        desktop_app.run()








