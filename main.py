MODE = 0 # 0 - webapp, 1 - desktopapp, 2 - testing

if __name__ == "__main__":
    if MODE == 0:
        from src.Web.app import app
        app.run(host="0.0.0.0", port=5000)
    elif MODE == 1:
        from src.DesktopApplication import DesktopApplication
        desktop_app = DesktopApplication()
        desktop_app.run()
    else:
        pass
        








