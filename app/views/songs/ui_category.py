from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QMessageBox, QTableView
from PySide6.QtCore import Qt

from app.exceptions.base_exception import AppError
from app.exceptions.business_exception import ValidationError
from app.views.shared.confirm_delete import ConfirmDelete
from app.views.songs.model_table.category_table import CategoryTableModel
from app.views.user_dialog.dialog_error import ErrorDialog
from app.controllers.category_controller import CategoryController

from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/category.ui"

class CategoryUI(QWidget):
    def __init__(self, session):
        super().__init__()
        self.ui = load_ui(UI_PATH)
        self.controller = CategoryController(session)

        """
        form config: bottun and input
        """
        self.btn_cancel = self.ui.findChild(QPushButton, "btn_cancel")
        self.btn_to_song = self.ui.findChild(QPushButton, "btn_to_lyric")
        self.btn_add_category = self.ui.findChild(QPushButton, 'btn_add_category')
        self.input_category_name = self.ui.findChild(QLineEdit, 'input_category_name')

        self.btn_add_category.clicked.connect(lambda: self.add_category())
        self.btn_cancel.clicked.connect(lambda: self.reset_defautl_ui())




        """
        delete & update button
        """
        self.btn_update = self.ui.findChild(QPushButton, "btn_update")
        self.btn_delete = self.ui.findChild(QPushButton, "btn_delete")

        self.btn_update.clicked.connect(lambda: self.update_category())
        self.btn_delete.clicked.connect(lambda: self.delete_category())

        self.updated_category = None



        """
        tableview configuration
        """

        self.table_categories = self.ui.findChild(QTableView, "table_categories")
        self.load_data()

    def get_ui(self):
        return self.ui
    

    def update_category(self):
        index = self.table_categories.currentIndex()
        category = self.model.data(index, Qt.UserRole)

        if category :
            self.btn_add_category.setText("Sauvegarder")
            self.input_category_name.setText(category.name)
            self.updated_category = category

    def delete_category(self):
        indexes = self.table_categories.selectionModel().selectedRows()

        confirm = ConfirmDelete(indexes)

        if confirm.execute():
            for index in indexes:
                category = self.model.data(index, Qt.UserRole)
                if category :
                    try:
                        self.controller.delete_category(category.id)
                        QMessageBox.information(
                            self,
                            "Succès",
                            f"Suppression de {len(indexes)} éléments avec succès."
                        )
                    except AppError as e :
                        error_dialog = ErrorDialog(self, type='critical', exception=e)
                        error_dialog.show()
            
            self.reset_defautl_ui()
            

    def add_category(self):
        category_name = self.input_category_name

        try:
            if not self.updated_category :
                self.controller.add_category(category_name.text())
                QMessageBox.information(
                    self,
                    "Succès",
                    f"La catégorie '{category_name.text()}' a été ajoutée avec succès."
                )
            else : 
                self.controller.update_category(id=self.updated_category.id, name=category_name.text())
                QMessageBox.information(
                    self,
                    "Succès",
                    f"La catégorie '{self.updated_category.name}' a été modifiée avec succès."
                )
                
        except ValidationError as e:
            error_dialog = ErrorDialog(self, type='warning', exception=e)
            error_dialog.show()
        except AppError as e :
            error_dialog = ErrorDialog(self, type='critical', exception=e)
            error_dialog.show()
        finally:
            self.reset_defautl_ui()
    
    def reset_defautl_ui(self):
        self.reset_buttons()
        self.load_data()
        self.input_category_name.setText("")
        self.updated_category = None

    def reset_buttons(self):
        self.btn_add_category.setText("Ajouter")
        self.btn_delete.setEnabled(False)
        self.btn_update.setEnabled(False)
    
    def load_data(self):
        self.model = CategoryTableModel(self.controller.get_categories())
        self.table_view_setup()
        
    
    def table_view_setup(self):
        self.table_categories.setModel(self.model)
        selection_model = self.table_categories.selectionModel()
        selection_model.selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        has_selection = self.table_categories.selectionModel().hasSelection()

        self.btn_delete.setEnabled(has_selection)
        self.btn_update.setEnabled(has_selection)

        
            