from src.Models.scraper import Scraper
from src.Models.scraperv2 import ScraperV2
from src.Desktop.View.ViewMain import ViewMain

import threading
from copy import deepcopy
from typing import List


class AppController:

    def __init__(self, *args, view: ViewMain = None, model: Scraper | ScraperV2 = None, **kwargs):
        self.view = view
        self.model = model
        self._connect_buttons()


    def start_scraping(self) -> None:
        """
        Reads the input from the text edit and starts the scraping process.
        """
        try:
            items = self._read_input()
        except Exception as exception_input:
            print(exception_input)

        self.run_threads(items)

    def run_threads(self, items: List[str]) -> None:
        """
        Runs scraping tasks in separate threads for each item in the list.
        """
        if len(items):
            self.view.bt_start.setEnabled(False)
            for item in items:
                thread = threading.Thread(target=self._run_task, args=(item, self.view.directory))
                thread.start()
        self.view.bt_start.setEnabled(True)


    def _read_input(self) -> List[str]:
        items = [item for item in self.view.te_words.toPlainText().split("\n") if item not in ["", "\n", " ", "\t"]]
        return items
    
    def _run_task(self, text: str, directory: str) -> None:
        model_instance = deepcopy(self.model)
        model_instance.execute_and_encode(text, directory)

    def _connect_buttons(self) -> None:
        self.view.bt_start.clicked.connect(self.start_scraping)

        