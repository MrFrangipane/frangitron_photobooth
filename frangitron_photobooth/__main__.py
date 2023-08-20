import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication()

main_window = QMainWindow()
main_window.setWindowTitle("Frangitron Photobooth")
main_window.showMaximized()

sys.exit(app.exec())

"""
from tdcdesktopapp.api import configuration
from tdcdesktopapp.ui.main_window import MainWindow


configuration.configure_for_ram()

app = QApplication()

main_window = MainWindow()
main_window.show()

sys.exit(app.exec())
"""
