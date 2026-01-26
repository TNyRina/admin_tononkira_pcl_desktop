from PySide6.QtWidgets import QWidget, QTableView

from app.controllers.controller import Controller
from app.views.songs.model_table.models.model_category_table import CategoryTableModel
from app.views.songs.model_table.tables.table_view import TableView

class CategoryTable(TableView):
    def __init__(self, parent: QWidget, controller):
        super().__init__(
            parent=parent,
            controller=controller,
            table_name="table_categories"
        )

    def set_model(self) -> None:
        self.model = CategoryTableModel(
            self.controller.get_categories()
        )

