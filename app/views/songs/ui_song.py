from PySide6.QtWidgets import QPushButton, QWidget, QTableView, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt
from app.controllers.song_controller import SongController
from app.exceptions.base_exception import AppError
from app.views.shared.confirm_delete import ConfirmDelete
from app.views.songs.model_table.song_table import SongTableModel
from app.views.songs.ui_form_add import FormAddSongUI
from app.views.user_dialog.dialog_error import ErrorDialog
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/songs/song.ui"

class SongUI(QWidget):
    def __init__(self, session):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        self.form_add_ui = FormAddSongUI(session)
        self.controller = SongController(session)

        self.btn_to_add_form = self.ui.findChild(QPushButton, "btn_to_add_form")
        self.btn_to_category = self.ui.findChild(QPushButton, "btn_to_category")

        self.btn_delete = self.ui.findChild(QPushButton, 'btn_delete')
        self.btn_update = self.ui.findChild(QPushButton, 'btn_update')
        self.btn_delete.clicked.connect(lambda: self.delete_songs())



        self.table_songs = self.ui.findChild(QTableView, 'table_songs')
        self.table_model = SongTableModel(self.controller.get_songs())
        self.table_songs.setModel(self.table_model)
        self.table_songs.setSelectionBehavior(QAbstractItemView.SelectRows)
        selection_model = self.table_songs.selectionModel()
        selection_model.selectionChanged.connect(self.on_selection_changed)

    def get_ui(self):
        return self.ui
    
    def on_selection_changed(self, selected, deselected):
        has_selection = self.table_songs.selectionModel().hasSelection()

        self.btn_delete.setEnabled(has_selection)
        self.btn_update.setEnabled(has_selection)
    
    def delete_songs(self):
        indexes = self.table_songs.selectionModel().selectedRows()
        print(f"selectedRows : {indexes}")
        confirme = ConfirmDelete(indexes)
        if confirme.execute() :
            for index in indexes :
                song = self.table_model.data(index, Qt.UserRole)
                if song :
                    try:
                        self.controller.delete_song(song.id)
                        QMessageBox.information(
                            self,
                            "Succès",
                            f"Suppression de {len(indexes)} éléments avec succès."
                        )
                    except AppError as e:
                        error_dialog = ErrorDialog(self, type='critical', exception=e)
                        error_dialog.show()
        