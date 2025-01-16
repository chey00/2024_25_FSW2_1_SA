from time import sleep

from PyQt6.QtCore import pyqtSlot, QFile, QIODevice, QTextStream, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QProgressBar, QStatusBar, QLabel, QMenuBar, QFileDialog, QMessageBox

from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        central_widget = CentralWidget(self)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("Temperaturüberwachung")
        self.setFixedSize(800, 800)

        self.__progress_bar = QProgressBar()
        self.__label = QLabel("No file loaded")

        status_bar = QStatusBar()
        status_bar.addWidget(self.__label)
        status_bar.addWidget(self.__progress_bar)

        self.setStatusBar(status_bar)

        menu_bar = QMenuBar()
        menu_bar.addAction("Datei öffnen...", self.open_file)

        self.setMenuBar(menu_bar)

        self.__initial_filter = "Log files (*.log)"
        self.__filter = self.__initial_filter + ";;All files (*)"

        self.__directory = ""

    @pyqtSlot()
    def open_file(self):
        (path, self.__initial_filter) = QFileDialog.getOpenFileName(self, "Open File", self.__directory, self.__filter,
                                                                    self.__initial_filter)

        if path:
            self.__directory = path[:path.rfind("/")]
            self.__label.setText(path[path.rfind("/") + 1:])

            file = QFile(path)

            if not file.open(QIODevice.OpenModeFlag.ReadOnly):
                QMessageBox.information(self, "Unable to open file", file.errorString())

                return

            stream = QTextStream(file)
            text_in_file = stream.readAll()

            lines = text_in_file.split("\n")

            self.__progress_bar.setRange(0, len(lines))

            for i in range(len(lines)):
                self.__progress_bar.setValue(i + 1)

            file.close()
