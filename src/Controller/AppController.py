import threading


from src.Models.scraper import Scraper
from src.View.UI.ViewMain import ViewMain

from typing import List


class AppController:

    def __init__(self, *args, view: ViewMain = None, model: Scraper = None, **kwargs):
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


    def _read_input(self) -> List[str]:
        items = [item for item in self.view.te_words.toPlainText().split("\n") if item not in ["", "\n", " ", "\t"]]
        return items
    
    def _run_task(self, text: str, directory: str) -> None:
        Scraper(text, directory)

    def _connect_buttons(self) -> None:
        self.view.bt_start.clicked.connect(self.start_scraping)

        