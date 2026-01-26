from PySide6.QtWidgets import QTableView, QWidget

from app.controllers.controller import Controller
from app.views.songs.model_table.models.model_song_table import SongTableModel
from app.views.songs.model_table.tables.table_view import TableView

class SongTable(TableView):
    def __init__(self, parent: QWidget, controller: Controller) :
        super().__init__(
            parent=parent,
            controller=controller,
            table_name="table_songs"
        )


    def set_model(self) -> None :
        self.model = SongTableModel(
            self.controller.get_songs()
        )