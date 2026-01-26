from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QModelIndex

class ConfirmDelete():
    def __init__(self, indexes: list[QModelIndex]):
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(QMessageBox.Warning)  
        self.msg_box.setWindowTitle("Confirmation")
        self.msg_box.setText(f"Attention! vous allez supprimer {len(indexes)} éléments")
        self.msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg_box.setDefaultButton(QMessageBox.No) 


    def execute(self) -> bool:
        result = self.msg_box.exec()

        return result == QMessageBox.Yes