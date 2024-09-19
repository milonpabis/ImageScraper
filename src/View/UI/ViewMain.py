from src.View.UI.ViewTemplate import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

from static import DIR


class ViewMain(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setWindowTitle("GoogleImageScraper")
        self.setFixedSize(800, 600)

        self._setup_text_edit()
        self._setup_backgrounds()
        self._setup_icons()

        self.directory = DIR
        self.bt_dir.clicked.connect(self.dir_change)


    def dir_change(self) -> None:
        dialog = QFileDialog().getExistingDirectory()
        self.directory = dialog


    def _setup_text_edit(self) -> None:
        self.te_words.setStyleSheet("text-transform: uppercase; color: white;")
        self.te_words.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.te_words.setFontWeight(99)
        font = self.te_words.font()
        font.setPointSize(14)  # Adjust the size as needed
        font.setBold(True)
        self.te_words.setFont(font)
        
    def _setup_backgrounds(self) -> None:
        self.frame.setStyleSheet('#frame{background-image: url("src/View/UI/static/gray_bg.jpg");}')
        self.frame_2.setStyleSheet('#frame_2{background-image: url("src/View/UI/static/words.jpg");}')
        self.frame_3.setStyleSheet('#frame_3{background-image: url("src/View/UI/static/gray_bg.jpg");}')

    def _setup_icons(self) -> None:
        self.setWindowIcon(QIcon('src/View/UI/static/google_logo.png')) # window icon

        # logo
        self.l_logo.setPixmap(QPixmap("src/View/UI/static/google_logo.png"))
        self.l_logo.setScaledContents(True)

        #buttons
        self.bt_start.setIcon(QIcon("src/View/UI/static/button.png"))
        self.bt_dir.setIcon(QIcon("src/View/UI/static/directory.png"))