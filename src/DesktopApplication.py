from PySide6.QtWidgets import QApplication
from src.Desktop.View.ViewMain import ViewMain
from src.Models.scraper import Scraper
from src.Desktop.Controller.AppController import AppController


class DesktopApplication(QApplication):
    def __init__(self):
        super().__init__([])
        self.view = ViewMain()
        self.model = Scraper()
        self.controller = AppController(view=self.view, model=self.model)

    def run(self):
        self.view.show()
        self.exec()