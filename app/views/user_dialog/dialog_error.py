from PySide6.QtWidgets import QMessageBox
from app.views.user_dialog.dialog_message import ERROR_MESSAGES

class ErrorDialog:
    def __init__(self, parent, type,  exception):
        self.parent = parent
        self.code = exception.code
        self.exception = exception
        self.type = type
        

    def show(self):
        if self.type == 'warning' :
            QMessageBox.warning(
                    self.parent,
                    "Erreur",
                    f"{ERROR_MESSAGES[self.code]}"
                )
        
        if self.type == 'critical' :
            QMessageBox.critical(
                    self.parent,
                    "Critique",
                    f"{ERROR_MESSAGES[self.code]}"
                )

