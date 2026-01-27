from PySide6.QtWidgets import QTableView, QWidget, QAbstractItemView
from abc import abstractmethod

from app.controllers.controller import Controller

class TableView(QTableView):
    def __init__(
        self,
        parent: QWidget,
        controller: Controller,
        table_name: str
    ):
        super().__init__()


        """
        Data controller
        ==================================
        """
        
        self.controller = controller



        """
        Load widget
        ==================================
        """
        
        self.parent = parent
        self.widget = parent.ui.findChild(QTableView, table_name)



        """
        Create table model
        ==================================
        """
        self.widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.reset()

    @abstractmethod
    def set_model(self) -> None:
        pass

    def reset(self) -> None:
        self.set_model()
        self.widget.setModel(self.model)

        selection_model = self.widget.selectionModel()
        selection_model.selectionChanged.connect(self._on_selection_changed)


    def _on_selection_changed(self, selected, deselected) -> None:
        has_selection = self.widget.selectionModel().hasSelection()
        self.parent.btn_delete.setEnabled(has_selection)
        self.parent.btn_update.setEnabled(has_selection)
