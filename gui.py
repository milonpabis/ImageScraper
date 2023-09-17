from PySide6.QtGui import (QIcon, QColor, QFont, QImage, QPixmap, QLinearGradient, QPalette)
from PySide6.QtCore import Qt, QSize, QThread, Signal, QRunnable, QThreadPool, Slot
from PySide6.QtWidgets import (QWidget, QApplication, QMainWindow, QGridLayout, QSlider, QLabel, QFileDialog,
                               QPushButton, QVBoxLayout, QLineEdit)
import threading
from scraper import Scraper

LOGO = 'images/google_logo.png'


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GoogleImageScraper")
        self.setFixedSize(QSize(400, 600))
        self.setWindowIcon(QIcon(LOGO))
        self.pool = QThreadPool()

        # ---------------------------------------------------------------------- WINDOW GRADIENT
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#8E2DE2"))
        gradient.setColorAt(1, QColor("#4A00E0"))
        palette = self.palette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)



        label = QLabel()
        grid = QVBoxLayout()
        grid.setSpacing(0)

        logo = Image('images/google_logo.png', 100, 100)
        logo.setContentsMargins(0, 0, 0, 0)


        main_text = QLabel("Images Downloader")
        main_text.setContentsMargins(0, 0, 0, 0)
        main_text.setFont(QFont("Times", 28, QFont.Bold))
        main_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_text.setStyleSheet("color: white;")


        main_text1 = QLabel("Image name:")
        main_text1.setContentsMargins(0, 0, 0, 5)
        main_text1.setFont(QFont("Times", 14, QFont.Bold))
        main_text1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_text1.setStyleSheet("color: white;")


        self.input = QLineEdit()
        self.input.setFixedSize(QSize(150, 30))
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input.setStyleSheet("border: 1px solid gray;")

        self.button = QPushButton()
        self.button.setIcon(QIcon('images/button.png'))
        self.button.setIconSize(QSize(80, 80))
        self.button.setFixedSize(QSize(80, 80))
        self.button.setStyleSheet('border-radius: {}px;'.format(650 // 2))

        self.button.pressed.connect(self.button_clicked)





        grid.addWidget(logo, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid.addWidget(main_text, alignment=Qt.AlignmentFlag.AlignTop)
        grid.addWidget(main_text1, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        grid.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        grid.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        label.setLayout(grid)

        self.setCentralWidget(label)


    def button_clicked(self):
        item = self.input.text()
        if len(item) > 1:
            self.button.setEnabled(False)
            thread = ScraperThread(item)
            self.pool.start(thread)




class Image(QLabel):

    def __init__(self, path, height, width):
        super().__init__()
        self.setFixedSize(QSize(height, width))
        self.setScaledContents(True)
        self.change_image(path)
        self.setContentsMargins(0, 0, 0, 0)

    def change_image(self, path):
        pixmap = QPixmap(path)
        self.setPixmap(pixmap)


class ScraperThread(QRunnable):

    def __init__(self, item):
        super().__init__()
        self.item = item

    @Slot()
    def run(self):
        Scraper(self.item)








