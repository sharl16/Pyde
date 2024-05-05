import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyde")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        #load html
        current_dir = QtCore.QDir.currentPath()
        index_html = QtCore.QUrl.fromLocalFile(current_dir + "/editor/index.html")
        self.web_view.setUrl(index_html)

def show_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
