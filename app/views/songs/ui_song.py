from PySide6.QtWidgets import QPushButton, QWidget,QMessageBox
from PySide6.QtCore import Qt, QModelIndex
from app.controllers.song_controller import SongController
from app.exceptions.base_exception import AppError
from app.views.shared.confirm_delete import ConfirmDelete
from app.views.songs.model_table.tables.table_song import SongTable
from app.views.songs.ui_category import CategoryUI
from app.views.songs.form.ui_form_add import FormAddSongUI
from app.views.user_dialog.dialog_error import ErrorDialog
from app.views.utility.navigation import Navigation
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/songs/song.ui"

class SongUI(QWidget):
    def __init__(self, session, stack: QWidget):
        super().__init__()

        """
        Data controller
        ===================================
        """
        
        self.controller = SongController(session)



        """
        Load widget 
        ===================================
        """
        
        self.stack = stack
        self.ui = load_ui(UI_PATH)
        self.stack.addWidget(self.ui)



        
        """
        Navigation
        ===================================
        """
        
        self.nagivate = Navigation(stack = stack)




        """
        Subpages 
        ====================================
        """
        
        self.category_ui = CategoryUI(session=session, stack=self.stack, parent=self)
        self.form_add_ui = FormAddSongUI(session=session, stack=self.stack, parent=self)



        """
        Buttons navigation setup 
        ================================
        """
        
        # Button to add form page
        self.btn_to_add_form = self.ui.findChild(QPushButton, "btn_to_add_form")
        self.btn_to_add_form.clicked.connect(lambda: self.nagivate.goto(self.form_add_ui.get_ui()))

        # Button to category page
        self.btn_to_category = self.ui.findChild(QPushButton, "btn_to_category")
        self.btn_to_category.clicked.connect(lambda: self.nagivate.goto(self.category_ui.get_ui()))



        """
        Buttons setup
        =================================
        """
        

        self.btn_delete = self.ui.findChild(QPushButton, 'btn_delete')
        self.btn_delete.clicked.connect(lambda: self._confirm_delete())
        
        self.btn_update = self.ui.findChild(QPushButton, 'btn_update')


        """
        Tableview
        """
        

        self.table = SongTable(parent=self, controller= self.controller)

    def get_ui(self) -> QWidget:
        return self.ui
    
    def _confirm_delete(self):
        indexes = self.table.widget.selectionModel().selectedRows()
        confirme = ConfirmDelete(indexes)
        if confirme.execute() :
            self._delete_songs(indexes)
    
    def _delete_songs(self, indexes: list[QModelIndex]) -> None:
        for index in indexes :
            song = self.table.model.data(index, Qt.UserRole)
            if song :
                try:
                    self.controller.delete_song(song.id)
                    QMessageBox.information(
                        self,
                        "Succès",
                        f"Suppression de {len(indexes)} éléments avec succès."
                    )
                    self._reset_default_ui()
                except AppError as e:
                    error_dialog = ErrorDialog(self, type='critical', exception=e)
                    error_dialog.show()
    
    def _reset_default_ui(self):
        self.table.reset()
        self._reset_buttons()

    def _reset_buttons(self):
        self.btn_delete.setEnabled(False)
        self.btn_update.setEnabled(False)
        