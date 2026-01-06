from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QMessageBox
from app.exceptions.base import AppError
from app.exceptions.business import ValidationError
from app.views.utility.utils import load_ui
from app.controllers.category_controller import CategoryController

UI_PATH = "app/ui/songs/category.ui"

class CategoryUI(QWidget):
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.ui = load_ui(UI_PATH)

        self.btn_to_song = self.ui.findChild(QPushButton, "btn_to_lyric")
        self.btn_add_category = self.ui.findChild(QPushButton, 'btn_add_category')
        self.input_category_name = self.ui.findChild(QLineEdit, 'input_category_name')

        self.btn_add_category.clicked.connect(lambda: self._add_category())

    def get_ui(self):
        return self.ui
    
    def _add_category(self):
        category_name = self.input_category_name

        try:
            category_controller = CategoryController(self.session)
            category_controller.add_category(category_name.text())
            QMessageBox.information(
                self,
                "Succès",
                f"La catégorie '{category_name.text()}' a été ajoutée avec succès."
            )
            category_name.setText("")
        except ValidationError as e:
            QMessageBox.warning(
                self,
                "Erreur",
                e.message
            )
        except AppError:
            QMessageBox.critical(
                self,
                "Erreur",
                "Une erreur est survenue"
            )
        
        
            