from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def load_ui(path) -> QWidget:
        loader = QUiLoader()
        file = QFile(path)
        file.open(QFile.ReadOnly)
        ui = loader.load(file)
        file.close()

        return ui