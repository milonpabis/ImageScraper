from src.View.gui import Gui, QApplication
from src.Models.scraper import Scraper
from src.Controller.AppController import AppController


from src.View.UI.ViewMain import ViewMain

UI_TEST = 1

if __name__ == "__main__":
    if UI_TEST:
        app = QApplication()
        gui = ViewMain()
        gui.show()
        app.exec()
    else:
        controller = AppController(view=Gui(), model=Scraper())








