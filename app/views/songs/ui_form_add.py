from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QCheckBox,QLineEdit, QMessageBox
from app.controllers.category_controller import CategoryController
from app.controllers.song_controller import SongController
from app.views.shared.flow_layout import FlowLayout
from app.views.user_dialog.dialog_error import ErrorDialog
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/form_add.ui"

class FormAddSongUI(QWidget):
    def __init__(self, session):
        super().__init__()
        self.ui = load_ui(UI_PATH)
        self.controller = SongController(session)


        self.input_title = self.ui.findChild(QLineEdit, 'input_title')
        self.input_author = self.ui.findChild(QLineEdit, 'input_author')
        self.input_composer = self.ui.findChild(QLineEdit, 'input_composer')
        self.input_description = self.ui.findChild(QTextEdit, 'text_description')
        self.input_refrain = self.ui.findChild(QTextEdit, 'text_refrain')


        self.btn_save = self.ui.findChild(QPushButton, 'btn_save')
        self.btn_save.clicked.connect(lambda: self.save_song())

        """
        Verses management
        """
        
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
    
    def save_song(self):
        title = self.input_title.text()
        author = self.input_author.text()
        composer = self.input_composer.text()
        description = self.input_description.toPlainText()
        refrain = self.input_refrain.toPlainText()

        verses = self.get_verses()

        layout_categories = self.categories_content.layout()
        selected_categories = []
        if layout_categories:
            for i in range(layout_categories.count()):
                checkbox = layout_categories.itemAt(i).widget()
                if checkbox.isChecked():
                    selected_categories.append(checkbox.property("value"))
        
        try:
            self.controller.add_song(
                title=title,
                release="",
                author=author,
                composer=composer,
                description=description,
                refrain=refrain,
                verse=verses,
                categories=selected_categories
            )
            QMessageBox.information(
                    self,
                    "Succès",
                    f"Lyric '{title}' a été ajoutée avec succès."
                )
        except Exception as e:
            error_dialog = ErrorDialog(self, type='warning', exception=e)
            error_dialog.show()

    def get_verses(self):
        layout_verses = self.content_verse.layout()
        verses = []

        if not layout_verses:
            return verses

        for i in range(layout_verses.count()):
            item = layout_verses.itemAt(i)
            verse_widget = item.widget().layout()
            if verse_widget:
                text_edit = verse_widget.itemAt(1).widget()
                verses.append(text_edit.toPlainText())


        return verses

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
