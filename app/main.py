from PySide6.QtWidgets import QApplication

import sys
from app.views.ui_main_window import MainWindow

TITLE_APP = "PCL | Petits Chanteurs de la Louange"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(TITLE_APP)
    window.show()
    app.exec() 