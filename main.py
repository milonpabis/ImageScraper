from gui import Gui, QApplication
#from scraper import Scraper



#TODO:
# - GUI
# - ends the scrolling loop when it is an end
# - getting default user path to desktop

#scraper = Scraper('Pilka')
if __name__ == "__main__":
    #Scraper("card queen of spades")
    app = QApplication()
    gui = Gui()
    gui.show()

    app.exec()








