from PySide6.QtWidgets import QApplication
import sys
from app.db import SessionLocal
from app.views.ui_main_window import MainWindow

TITLE_APP = "PCL | Petits Chanteurs de la Louange"
session = SessionLocal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(TITLE_APP, session)
    window.show()
    app.exec() 