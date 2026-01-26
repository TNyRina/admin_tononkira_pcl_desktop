from PySide6.QtWidgets import QWidget, QCheckBox

from app.controllers.category_controller import CategoryController
from app.views.shared.flow_layout import FlowLayout

class BoxCategories(QWidget):
    def __init__(self, session,  parent: QWidget):
        super().__init__()


        """
        Load UI
        =================================
        """
        
        self.ui = parent.get_ui().findChild(QWidget, 'categories_content')




        """
        Setup layout
        """
        
        flow_layout = FlowLayout(self.ui)
        self.ui.setLayout(flow_layout)
        
        category_controller = CategoryController(session)
        categories = category_controller.get_categories()

        for cat in categories:
            self.add_checkbox(flow_layout, cat)


    def add_checkbox(self, container, checkbox_value):
        checkbox = QCheckBox(checkbox_value.name)
        checkbox.setProperty("value", checkbox_value.id)
        container.addWidget(checkbox)  
    
    def get_selected_boxes(self) -> list:
        layout_categories = self.ui.layout()
        selected_categories = []
        if layout_categories:
            for i in range(layout_categories.count()):
                checkbox = layout_categories.itemAt(i).widget()
                if checkbox.isChecked():
                    selected_categories.append(checkbox.property("value"))

        return selected_categories