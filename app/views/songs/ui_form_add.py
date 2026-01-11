from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QCheckBox
from app.controllers.category_controller import CategoryController
from app.views.shared.flow_layout import FlowLayout
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/form_add.ui"

class FormAddSongUI(QWidget):
    def __init__(self, session):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        self.btn_push_verse = self.ui.findChild(QPushButton, 'btn_push_verse')
        self.btn_pop_verse = self.ui.findChild(QPushButton, 'btn_pop_verse')
        self.content_verse = self.ui.findChild(QWidget, 'content_verses')
        
        self.btn_push_verse.clicked.connect(lambda: self._push_verse())
        self.btn_pop_verse.clicked.connect(lambda: self._pop_verse())

        """
        Categories options
        """
        self.categories_content = self.ui.findChild(QWidget, 'categories_content')
        self.setup_categories_checkboxes(session)
        
    def setup_categories_checkboxes(self, session):
        flow_layout = FlowLayout(self.categories_content)
        self.categories_content.setLayout(flow_layout)
        
        category_controller = CategoryController(session)
        categories = category_controller.get_categories()

        for cat in categories:
            self.add_checkbox(flow_layout, cat)

    def add_checkbox(self, container, checkbox_value):
        checkbox = QCheckBox(checkbox_value.name)
        checkbox.setProperty("value", checkbox_value.id)
        container.addWidget(checkbox)  

    def get_ui(self):
        return self.ui

    def _push_verse(self):
        layout_content = self.content_verse.layout()

        if layout_content is None:
            layout_content = QVBoxLayout(self.content_verse)

        index = layout_content.count() + 1

        verse_widget = QWidget()
        verse_layout = QVBoxLayout(verse_widget)

        label = QLabel(f"Verse {index}")
        text = QTextEdit()
        text.setObjectName(f"text_verse_{index}")

        verse_layout.addWidget(label)
        verse_layout.addWidget(text)

        layout_content.addWidget(verse_widget)

    def _pop_verse(self):
        layout = self.content_verse.layout()

        if layout is None or layout.count() <= 1:
            return 

        item = layout.takeAt(layout.count() - 1)
        if item.widget():
            item.widget().deleteLater()
