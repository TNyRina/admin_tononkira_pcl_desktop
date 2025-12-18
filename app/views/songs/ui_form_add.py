from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/form_add.ui"

class FormAddSongUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        self.btn_push_verse = self.ui.findChild(QPushButton, 'btn_push_verse')
        self.btn_pop_verse = self.ui.findChild(QPushButton, 'btn_pop_verse')
        self.content_verse = self.ui.findChild(QWidget, 'content_verses')
        
        self.btn_push_verse.clicked.connect(lambda: self._push_verse())
        self.btn_pop_verse.clicked.connect(lambda: self._pop_verse())
        

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
