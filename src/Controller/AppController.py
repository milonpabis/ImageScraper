from src.Models.scraper import Scraper
from src.View.gui import Gui


class AppController:

    def __init__(self, *args, view=None, model=None, **kwargs):
        self.view = view
        self.model = model

        