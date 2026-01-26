from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, QModelIndex

from app.exceptions.base_exception import AppError
from app.exceptions.business_exception import ValidationError
from app.views.shared.confirm_delete import ConfirmDelete
from app.views.songs.model_table.tables.table_category import CategoryTable
from app.views.user_dialog.dialog_error import ErrorDialog
from app.controllers.category_controller import CategoryController

from app.views.utility.navigation import Navigation
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/category.ui"

class CategoryUI(QWidget):
    def __init__(self, session, stack: QWidget, parent: QWidget):
        super().__init__()
        self.controller = CategoryController(session)

        """
        Load page 
        =======================================
        """
        
        self.stack = stack
        self.ui = load_ui(UI_PATH)
        self.stack.addWidget(self.ui)




        """
        Navigation 
        ======================================
        """
        
        self.navigate = Navigation(stack= stack)




        """
        Buttons navigation
        =========================================
        """
        
        # Button to song page
        self.btn_to_song = self.ui.findChild(QPushButton, "btn_to_lyric")
        self.btn_to_song.clicked.connect(lambda: self.navigate.goto(parent.get_ui()))





        """
        Form configuration: bottun and input
        ========================================
        """

        # Cancel Button
        self.btn_cancel = self.ui.findChild(QPushButton, "btn_cancel")
        self.btn_cancel.clicked.connect(lambda: self.reset_defautl_ui())
        
        # Submit button
        self.btn_submit = self.ui.findChild(QPushButton, 'btn_submit')
        self.btn_submit.clicked.connect(lambda: self._submit_form())

        # Input name
        self.input_category_name = self.ui.findChild(QLineEdit, 'input_category_name')

        
    


        """
        Delete & update button
        ========================================
        """
        self.btn_update = self.ui.findChild(QPushButton, "btn_update")
        self.btn_update.clicked.connect(lambda: self._update_category())


        self.btn_delete = self.ui.findChild(QPushButton, "btn_delete")
        self.btn_delete.clicked.connect(lambda: self._confirm_delete())

        

        """
        Define form action 
        ==========================================
        form adds category if updated_category has value else form updates category

        type value : Category

        """
        
        self.updated_category = None



        """
        tableview configuration
        """
        self.table = CategoryTable(parent=self, controller=self.controller)

    
    def get_ui(self) -> None:
        return self.ui
    



    def _update_category(self) -> None:
        index = self.table.widget.currentIndex()
        category = self.table.model.data(index, Qt.UserRole)

        if category :
            self.btn_submit.setText("Sauvegarder")
            self.input_category_name.setText(category.name)
            self.updated_category = category




    def _confirm_delete(self) -> None:
        indexes = self.table.widget.selectionModel().selectedRows()

        confirm = ConfirmDelete(indexes)
        if confirm.execute():
            self._delete_category(indexes)
            
            

    def _delete_category(self, indexes: list[QModelIndex]) -> None:
        for index in indexes:
            category = self.table.model.data(index, Qt.UserRole)
            if category :
                try:
                    self.controller.delete_category(category.id)
                    QMessageBox.information(
                        self,
                        "Succès",
                        f"Suppression de {len(indexes)} éléments avec succès."
                    )
                    self._reset_defautl_ui()
                except AppError as e :
                    error_dialog = ErrorDialog(self, type='critical', exception=e)
                    error_dialog.show()
            
            

    def _submit_form(self) -> None:
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
            self._reset_defautl_ui()
    



    def _reset_defautl_ui(self) -> None:
        self._reset_form()
        self.table.reset()
        self.input_category_name.setText("")
        self.updated_category = None



    def _reset_form(self) -> None:
        self.btn_submit.setText("Ajouter")
        self.btn_delete.setEnabled(False)
        self.btn_update.setEnabled(False)
    

        
            